# !/usr/bin/env python
"""Script for streaming purchased TON PUNKS NFTs."""
import asyncio
import aiohttp
import math
import sys

from loguru import logger
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from util.disintar_curl_config import DisintarCurlConfigs

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


class TonPunkPurchaseChecker:
    """
    A class to represent a purchase checker for Ton Punk NFT
    """

    def __init__(self) -> None:
        """
        Init TonPunkPurchaseChecker instance

        :Args:
         - backup_ton_punks_state : List[TonPunkPurchase]
            backup TON PUNKS state
            use when exceptions was handled
         - previous_ton_punks_state : List[TonPunkPurchase]
            TON PUNKS state that used to compare previous state with current
         - current_ton_punks_state : List[TonPunkPurchase]
            TON PUNKS state that used to compare current state with previous
        """

        self.__backup_ton_punks_state: List[TonPunkPurchase] = []
        self.__previous_ton_punks_state: List[TonPunkPurchase] = []
        self.__current_ton_punks_state: List[TonPunkPurchase] = []
        self.__is_current_state: bool = False
        self.__config: DisintarCurlConfigs = DisintarCurlConfigs({}, {})

    async def __gather_data(self, is_current_state: bool) -> None:
        """
        Async call to _load_page_content()

        :Args:
         - is_current_state: bool - check if this state is current
        """

        self.__is_current_state = is_current_state

        await asyncio.gather(*[self.__load_page_content(page) for page in range(self.__config.COUNT_OF_PAGES)])

    async def __load_page_content(self, page: int) -> None:
        """
        Async load content of the page with NFTs

        :Args:
         - page: int - number of the page with NFTs
        """

        async with aiohttp.ClientSession() as session:
            response = await session.post(
                url=self.__config.API_URL,
                cookies=self.__config.cookies,
                headers=self.__config.headers,
                data=self.__config.data(page)
            )
            await self.__parse_nfts(await response.json())

    async def __parse_nfts(self, json_response: Any) -> None:
        """
        Async call to _parse_nft()

        :Args:
         - json_response: Any - response from page in json format
        """

        await asyncio.gather(*[self.__parse_nft(nft) for nft in json_response['data']])

    async def __parse_nft(self, nft: Dict[str, Any]) -> None:
        """
        Parse NFT to TonPunkPurchase and append it to the ${VERSION}_TON_PUNKS_STATE

        :Args:
         - nft: Dict[str, Any] - unparsed NFT
        """

        state = self.__current_ton_punks_state if self.__is_current_state else self.__previous_ton_punks_state

        state.append(TonPunkPurchase(
            name=nft['name'],
            price=None if nft['price'] is None else int(math.ceil(nft['price'])),
            address=nft['address'], owner=nft['owner']['wallet_address'],
            is_selling=nft['is_selling'])
        )

    def __get_purchased_nfts(self) -> List[TonPunkPurchase]:
        """
        Compare previous and current states with TON PUNKS
        Looking for the TON PUNKS state change
        Checks if TON PUNK matches the conditions

        :Return:
         - List[TonPunkPurchase] - return matches TON PUNKS
        """

        purchases_ton_punks: List[TonPunkPurchase] = []

        for matched in (current for current in enumerate(self.__current_ton_punks_state) if
                        current[1].is_selling and
                        current[1].price != self.__previous_ton_punks_state[current[0]].price):
            purchases_ton_punks.append(matched[1])

        return purchases_ton_punks

    def streaming_of_purchased_nfts(self) -> None:
        """
        Main application
        Streaming new purchases TON PUNKS NFTs
        """

        logger.info('Start streaming new purchases TON PUNKS NFTs')

        while True:
            try:
                asyncio.run(self.__gather_data(False)) \
                    if not self.__previous_ton_punks_state \
                    else asyncio.run(self.__gather_data(True))

                if not self.__current_ton_punks_state:
                    asyncio.run(self.__gather_data(True))
            except Exception as e:
                logger.error(e)
                logger.info('Reset csrf token')

                self.__config.reset_csrf()

                self.__previous_ton_punks_state = self.__backup_ton_punks_state
                self.__previous_ton_punks_state = []

                continue

            self.__previous_ton_punks_state = sorted(self.__previous_ton_punks_state, key=lambda punk: punk.name)
            self.__current_ton_punks_state = sorted(self.__current_ton_punks_state, key=lambda punk: punk.name)

            purchases_ton_punks = self.__get_purchased_nfts()

            if purchases_ton_punks:
                logger.info(f'Found {len(purchases_ton_punks)} new purchases TON PUNKS')

            self.__previous_ton_punks_state = self.__current_ton_punks_state
            self.__backup_ton_punks_state = self.__previous_ton_punks_state
            self.__current_ton_punks_state = []


def main() -> None:
    """
    Run script for streaming purchased TON PUNKS NFTs
    """

    TonPunkPurchaseChecker().streaming_of_purchased_nfts()


if __name__ == "__main__":
    main()
