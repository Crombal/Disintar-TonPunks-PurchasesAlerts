# !/usr/bin/env python
"""Script for loading DB of TON PUNKS NFTs."""
import asyncio
import aiohttp
import json
import sys

from bs4 import BeautifulSoup
from loguru import logger
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from util.time_measure_decorator import timeit
from config.disintar_curl_config import cookies, headers, URL, data

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')


class TonPunk(BaseModel):
    """
    A class to represent a Ton Punk NFT.

    ...

    Attributes
    ----------
    name : str
        name of the TON PUNK
    address : Optional[str]
        address of the TON PUNK
    rarity_score : Optional[float]
        rarity score of the TON PUNK
    rating_rank : Optional[int]
        rating rank of the TON PUNK
    """

    name: str
    address: Optional[str]
    rarity_score: Optional[float]
    rating_rank: Optional[int]


class TonPunkEncoder(json.JSONEncoder):
    """
    A class to represent a Ton Punk Json Encoder.
    """

    def default(self, obj: TonPunk) -> Any:
        if isinstance(obj, TonPunk):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class TonPunkDBCreator:
    """
    A class to represent a script for loading DB of TON PUNKS NFTs
    """

    def __init__(self, pages_count_disintar: int, nft_limit_per_page_disintar: int, pages_count_tonnft: int):
        """
        Init TonPunkPurchaseChecker instance

        :Args:
         - pages_count_disintar : int
            count of pages with TON PUNK NFTs at disintar.io
         - nft_limit_per_page_disintar : int
            limit of NFTs per page
         - pages_count_tonnft : int
            count of pages with TON PUNK NFTs at tonnft.tools
         - tonnft_db : List[TonPunk]
            TON PUNKS DB from tonnft.tools
         - disintar_db : List[TonPunkPurchase]
            TON PUNKS DB from disintar.io
         - ton_punks_db : List[TonPunk]
            TON PUNKS DB merged from tonnft_db and disintar_db
        """

        self.__pages_count_disintar = pages_count_disintar
        self.__nft_limit_per_page_disintar = nft_limit_per_page_disintar
        self.__pages_count_tonnft = pages_count_tonnft
        self.__tonnft_db: List[TonPunk] = []
        self.__disintar_db: List[TonPunk] = []
        self.__ton_punks_db: List[TonPunk] = []

    async def __gather_data_disintar(self) -> None:
        """
        Async call to __load_page_content_disintar()
        """

        await asyncio.gather(*[self.__load_page_content_disintar(page) for page in range(self.__pages_count_disintar)])

    async def __load_page_content_disintar(self, page: int) -> None:
        """
        Async load content of the page with NFTs from disintar.io

        :Args:
         - page: int - number of the page with NFTs
        """

        async with aiohttp.ClientSession() as session:
            response = await session.post(
                url=URL,
                cookies=cookies,
                headers=headers,
                data=data(page, self.__nft_limit_per_page_disintar)
            )
            await self.__parse_nfts_disintar(await response.json())

    async def __parse_nfts_disintar(self, json_response: Any) -> None:
        """
        Async call to __parse_nft_disintar()

        :Args:
         - json_response: Any - response from disintar page in json format
        """

        await asyncio.gather(*[self.__parse_nft_disintar(nft) for nft in json_response['data']])

    async def __parse_nft_disintar(self, nft: Dict[str, Any]) -> None:
        """
        Parse NFT to TonPunk and append it to the disintar_db

        :Args:
         - nft: Dict[str, Any] - unparsed NFT
        """

        self.__disintar_db.append(TonPunk(
            name=nft['name'],
            address=nft['address'],
            owner=nft['owner']['wallet_address']
        ))

    async def __gather_data_tonnft(self) -> None:
        """
        Async call to __load_page_content_tonnft()
        """

        await asyncio.gather(*[self.__load_page_content_tonnft(page)
                               for page in range(1, self.__pages_count_tonnft + 1)])

    async def __load_page_content_tonnft(self, page: int) -> None:
        """
        Async load content of the page with NFTs from tonnft.tools

        :Args:
         - page: int - number of the page with NFTs
        """

        async with aiohttp.ClientSession() as session:
            response = await session.get(f'https://tonnft.tools/collection/tonpunks?page={page}')
            await self.__parse_nfts_tonnft(await response.text())

    async def __parse_nfts_tonnft(self, page: Any) -> None:
        """
        Async call to __parse_nft_disintar()

        :Args:
         - json_response: Any - response from tonnft page
        """

        soup = BeautifulSoup(page, 'lxml')
        nfts = soup.find_all('div', class_='card text-decoration-none nftItemCard')
        await asyncio.gather(*[self.__parse_nft_tonnft(nft) for nft in nfts])

    async def __parse_nft_tonnft(self, nft: Any) -> None:
        """
        Parse NFT to TonPunk and append it to the tonnft_db

        :Args:
         - nft: Any - unparsed NFT
        """

        main_span = nft.find('span', class_='fs-3')
        spans = main_span.find_all('span')
        self.__tonnft_db.append(TonPunk(
            name=nft.find('h5', class_='card-title m-0').text,
            rarity_score=spans[0].text,
            rating_rank=spans[1].text[1:]
        ))

    async def __load_full_nfts(self) -> None:
        """
        Load DB with TON PUNKS NFTs
        """

        await asyncio.gather(*[self.__append_nft(nft) for nft in self.__tonnft_db])

    async def __append_nft(self, nft: TonPunk) -> None:
        """
        Find NFT in separate DB and append it to the ton_punks_db

        :Args:
         - nft: TonPunk - NFT to find
        """

        for disintar_nft in (
                disintar_nft for disintar_nft in self.__disintar_db
                if disintar_nft.name == nft.name):
            self.__ton_punks_db.append(TonPunk(
                name=disintar_nft.name,
                address=disintar_nft.address,
                rarity_score=nft.rarity_score,
                rating_rank=nft.rating_rank
            ))

    @timeit
    def create_db(self) -> None:
        """
        Create DB in json format
        """

        logger.info('Start NFTs loading')
        asyncio.run(self.__gather_data_disintar())
        logger.info(f'Disintar NFT DB size: {len(self.__disintar_db)}')
        asyncio.run(self.__gather_data_tonnft())
        logger.info(f'Tonnft NFT DB size: {len(self.__tonnft_db)}')
        asyncio.run(self.__load_full_nfts())
        logger.info(f'TON PUNKS DB size: {len(self.__ton_punks_db)}')

        with open("punks_db.json", "w") as json_db:
            json.dump(
                sorted(self.__ton_punks_db, key=lambda punk: punk.rating_rank),  # type: ignore
                json_db,
                cls=TonPunkEncoder
            )


def main() -> None:
    """
    Run script for loading DB of TON PUNKS NFTs
    """

    TonPunkDBCreator(256, 21, 129).create_db()


if __name__ == "__main__":
    main()
