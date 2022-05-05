# !/usr/bin/env python
"""Script for load config values from config file"""

import sys
import yaml
from pydantic import BaseModel
from loguru import logger

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')


class Config(BaseModel):
    """
    A class to represent a config.

    ...

    Attributes
    ----------
    TON_PUNKS_COLLECTION_URL : str
        The Ton Punks collection url on disintar.io
    LOAD_TIME : float
        Wait time of page load
    MAX_PRICE : int
        The maximum price up to which NFTs are searched for
    NFT_CARD_CONTAINER : str
        The class name of nft card container div
    NFT_CARD_META : str
        The class name of nft card meta div
    NFT_CARD_PRICE : str
        The class name of nft card price div
    NFT_CARD_TITLE : str
        The class name of nft card title h1
    """

    TON_PUNKS_COLLECTION_URL: str
    LOAD_TIME: float
    MAX_PRICE: int
    NFT_CARD_CONTAINER: str
    NFT_CARD_META: str
    NFT_CARD_PRICE: str
    NFT_CARD_TITLE: str

    def __str__(self) -> str:
        """This method returns the string representation of the Config"""
        return (f'TON_PUNKS_COLLECTION_URL: {self.TON_PUNKS_COLLECTION_URL}\n'
                f'LOAD_TIME: {self.LOAD_TIME}\n'
                f'MAX_PRICE: {self.MAX_PRICE}\n'
                f'NFT_CARD_CONTAINER: {self.NFT_CARD_CONTAINER}\n'
                f'NFT_CARD_META: {self.NFT_CARD_META}\n'
                f'NFT_CARD_PRICE: {self.NFT_CARD_PRICE}\n'
                f'NFT_CARD_TITLE: {self.NFT_CARD_TITLE}')


def _load_config() -> Config:
    """Load config values from config file and pass them to the Config"""
    config = yaml.safe_load(open("config.yaml"))

    DISINTAR = config['DISINTAR']
    DISINTAR_CLASS_NAME = DISINTAR['CLASS_NAME']
    DISINTAR_CLASS_NAME_DIV = DISINTAR_CLASS_NAME['DIV']
    DISINTAR_CLASS_NAME_H1 = DISINTAR_CLASS_NAME['H1']

    loaded_config = Config(TON_PUNKS_COLLECTION_URL=DISINTAR['TON_PUNKS_COLLECTION_URL'],
                           LOAD_TIME=DISINTAR['LOAD_TIME'],
                           MAX_PRICE=DISINTAR['MAX_PRICE'],
                           NFT_CARD_CONTAINER=DISINTAR_CLASS_NAME_DIV['NFT_CARD_CONTAINER'],
                           NFT_CARD_META=DISINTAR_CLASS_NAME_DIV['NFT_CARD_META'],
                           NFT_CARD_PRICE=DISINTAR_CLASS_NAME_DIV['NFT_CARD_PRICE'],
                           NFT_CARD_TITLE=DISINTAR_CLASS_NAME_H1['NFT_CARD_TITLE'])

    logger.info(f'Successfully loaded config:\n{loaded_config}')
    return loaded_config
