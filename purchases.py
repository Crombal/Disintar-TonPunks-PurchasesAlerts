# !/usr/bin/env python
"""Script for parse new purchases of TON PUNKS nfts on Disintar.io"""

import time
import sys
import bs4.element

from bs4 import BeautifulSoup, Tag
from loguru import logger
from config import Config
from config import _load_config
from driver import _load_driver
from typing import List
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from fake_useragent import UserAgent  # type: ignore
from webdriver_manager.firefox import GeckoDriverManager  # type: ignore

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')


class SurfaceTonPunkNFT(BaseModel):
    """
    A class to represent a Surface Ton Punk NFT.

    ...

    Attributes
    ----------
    name : str
        name of the NFT
    price : int
        price of the NFT
    """

    name: str
    price: int


CONFIG: Config = _load_config()
DRIVER: webdriver.Firefox = _load_driver().driver
SURFACE_NFTS_DB: List[SurfaceTonPunkNFT] = []


def _load_page(driver: webdriver.Firefox, url: str) -> None:
    """
    Load dynamic html page with NFTs while NFT`s price >= MAX_PRICE.

    :Args:
     - driver: webdriver.Firefox - Firefox web driver
     - url: str - Url of page with NFTs

    :Raises:
     - Exception - if the something went wrong with Firefox web driver
    """
    try:
        driver.get(url=url)
        logger.info(f'Driver go to the {url}')
        # Wait for load page
        time.sleep(CONFIG.DISINTAR_LOAD_TIME)
        # Get scroll height
        last_height = driver.execute_script('return document.body.scrollHeight')
        while _load_nfts(page=driver.page_source):
            # Scroll down to bottom
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            # Wait for load page
            time.sleep(CONFIG.DISINTAR_LOAD_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                break
            last_height = new_height
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def _load_nfts(page: str) -> bool:
    """
    Load NFTs surface data while NFT`s price >= MAX_PRICE.
    Add each unique NFT to in-memory list

    :Args:
     - page: str - Static html page with NFTs

    :Returns:
     - bool - if NFT`s price < 1500 return True, else - False
    """
    soup = BeautifulSoup(page, 'lxml')
    all_nfts = soup.find_all('div', class_=CONFIG.DISINTAR_CLASS_NAME_DIV_NFT_CARD_CONTAINER)
    unique_nfts = all_nfts if len(SURFACE_NFTS_DB) == 0 else all_nfts[len(SURFACE_NFTS_DB):]
    logger.info(f'Find {len(unique_nfts)} new unique NFTs')
    for nft_raw in unique_nfts:
        nft = _surface_parse_nft(nft_raw)
        if nft.price >= CONFIG.DISINTAR_MAX_PRICE:
            return False
        SURFACE_NFTS_DB.append(nft)
    return True


def _surface_parse_nft(nft_raw: Tag) -> SurfaceTonPunkNFT:
    """
    Surface NFT parsing

    :Args:
     - nft_raw: Tag - BS4 Tag

    :Returns:
     - SurfaceTonPunkNft - Surface parsed NFT
    """
    nft_meta_tag = nft_raw.find('div', class_=CONFIG.DISINTAR_CLASS_NAME_DIV_NFT_CARD_META)
    return SurfaceTonPunkNFT(
        name=nft_meta_tag.find('h1', class_=CONFIG.DISINTAR_CLASS_NAME_H1_NFT_CARD_TITLE).text,  # type: ignore
        price=nft_meta_tag.find('div',  # type: ignore
                                class_=CONFIG.DISINTAR_CLASS_NAME_DIV_NFT_CARD_PRICE).find('p').text.split(' ')[0]
    )


def main() -> None:
    _load_page(DRIVER, CONFIG.DISINTAR_TON_PUNKS_COLLECTION_URL)
    logger.info(f'Successfully surface parsed {len(SURFACE_NFTS_DB)} NFTs')


if __name__ == "__main__":
    main()
