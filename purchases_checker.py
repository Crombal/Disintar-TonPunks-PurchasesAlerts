import asyncio
import aiohttp
import math
import sys

from loguru import logger
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from config.disintar_curl_config import cookies, headers, URL, data

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')


class TonPunkPurchase(BaseModel):
    """
    A class to represent a purchase state of Ton Punk NFT.

    ...

    Attributes
    ----------
    name : str
        name of the TON PUNK
    price : Optional[int]
        price of the TON PUNK
    address : str
        address of the TON PUNK
    owner : str
        owner address of the TON PUNK
    is_selling : bool
        is the TON PUNK selling
    """

    name: str
    price: Optional[int]
    address: str
    owner: str
    is_selling: bool


async def _gather_data(pages_count: int, limit: int, state: List[TonPunkPurchase]) -> None:
    """
    Async call to _load_page_content()

    :Args:
     - state: List[TonPunkPurchase] - state with TON PUNKS
     - pages_count: int - count of the pages with NFTs
     - limit: int - limit of the NFTs per page
    """
    await asyncio.gather(*[_load_page_content(page, limit, state) for page in range(pages_count)])


async def _load_page_content(page: int, limit: int, state: List[TonPunkPurchase]) -> None:
    """
    Async load content of the page with NFTs

    :Args:
     - state: List[TonPunkPurchase] - state with TON PUNKS
     - page: int - number of the page with NFTs
     - limit: int - limit of NFTs per page
    """
    async with aiohttp.ClientSession() as session:
        response = await session.post(url=URL, cookies=cookies, headers=headers, data=data(page, limit))
        await _parse_nfts(await response.json(), state)


async def _parse_nfts(json_response: Any, state: List[TonPunkPurchase]) -> None:
    """
    Async call to _parse_nft()

    :Args:
     - state: List[TonPunkPurchase] - state with TON PUNKS
     - json_response: Any - response from page in json format
    """
    await asyncio.gather(*[_parse_nft(nft, state) for nft in json_response['data']])


async def _parse_nft(nft: Dict[str, Any], state: List[TonPunkPurchase]) -> None:
    """
    Parse NFT to TonPunkPurchase and append it to the ${VERSION}_TON_PUNKS_STATE

    :Args:
     - state: List[TonPunkPurchase] - state with TON PUNKS
     - nft: Dict[str, Any] - unparsed NFT
    """
    state.append(TonPunkPurchase(
        name=nft['name'],
        price=None if nft['price'] is None else int(math.ceil(nft['price'])),
        address=nft['address'], owner=nft['owner']['wallet_address'],
        is_selling=nft['is_selling'])
    )


def _get_purchased_nfts(previous_ton_punks_state: List[TonPunkPurchase],
                        current_ton_punks_state: List[TonPunkPurchase]) -> List[TonPunkPurchase]:
    """
    Compare previous and current states with TON PUNKS
    Looking for the TON PUNKS state change
    Checks if TON PUNK matches the conditions

    :Args:
     - previous_ton_punks_state: List[TonPunkPurchase] - previous TON PUNKS state
     - current_ton_punks_state: List[TonPunkPurchase] - current TON PUNKS state

    :Return:
     - List[TonPunkPurchase] - return matches TON PUNKS
    """
    purchases_ton_punks: List[TonPunkPurchase] = []

    for matched in (current for current in enumerate(current_ton_punks_state) if
                    current[1].is_selling and
                    current[1].price != previous_ton_punks_state[current[0]].price):
        purchases_ton_punks.append(matched[1])

    return purchases_ton_punks


def streaming_of_purchased_nfts() -> None:
    """
    Main application
    Streaming new purchases TON PUNKS NFTs
    """
    previous_ton_punks_state: List[TonPunkPurchase] = []
    current_ton_punks_state: List[TonPunkPurchase] = []

    logger.info('Start streaming new purchases TON PUNKS NFTs')

    while True:
        asyncio.run(_gather_data(256, 21, previous_ton_punks_state)) if not previous_ton_punks_state \
            else asyncio.run(_gather_data(256, 21, current_ton_punks_state))

        if not current_ton_punks_state:
            asyncio.run(_gather_data(256, 21, current_ton_punks_state))

        previous_ton_punks_state = sorted(previous_ton_punks_state, key=lambda punk: punk.name)
        current_ton_punks_state = sorted(current_ton_punks_state, key=lambda punk: punk.name)

        purchases_ton_punks = _get_purchased_nfts(previous_ton_punks_state, current_ton_punks_state)

        if purchases_ton_punks:
            logger.info(f'Found {len(purchases_ton_punks)} new purchases TON PUNKS')

        previous_ton_punks_state = current_ton_punks_state
        current_ton_punks_state = []


if __name__ == "__main__":
    streaming_of_purchased_nfts()
