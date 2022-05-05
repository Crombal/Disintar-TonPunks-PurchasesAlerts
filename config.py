# !/usr/bin/env python
"""Script for load config values from config file"""

import yaml
from pydantic import BaseModel


class Config(BaseModel):
    """
    A class to represent a config.

    ...

    Attributes
    ----------
    TON_PUNKS_COLLECTION_URL : str
        Ton Punks collection url on disintar.io
    LOAD_TIME : float
        Wait time of page load
    NFT_CARD_CONTAINER : str
        Class name of nft card container div
    NFT_CARD_META : str
        Class name of nft card meta div
    NFT_CARD_PRICE : str
        Class name of nft card price div
    NFT_CARD_TITLE : str
        Class name of nft card title h1
    """

    TON_PUNKS_COLLECTION_URL: str
    LOAD_TIME: float
    NFT_CARD_CONTAINER: str
    NFT_CARD_META: str
    NFT_CARD_PRICE: str
    NFT_CARD_TITLE: str


def _load_config() -> Config:
    """Load config values from config file and pass them to the Config"""
    config = yaml.safe_load(open("config.yaml"))

    DISINTAR = config['DISINTAR']
    DISINTAR_CLASS_NAME = DISINTAR['CLASS_NAME']
    DISINTAR_CLASS_NAME_DIV = DISINTAR_CLASS_NAME['DIV']
    DISINTAR_CLASS_NAME_H1 = DISINTAR_CLASS_NAME['H1']

    return Config(
        TON_PUNKS_COLLECTION_URL=DISINTAR['TON_PUNKS_COLLECTION_URL'],
        LOAD_TIME=DISINTAR['LOAD_TIME'],
        NFT_CARD_CONTAINER=DISINTAR_CLASS_NAME_DIV['NFT_CARD_CONTAINER'],
        NFT_CARD_META=DISINTAR_CLASS_NAME_DIV['NFT_CARD_META'],
        NFT_CARD_PRICE=DISINTAR_CLASS_NAME_DIV['NFT_CARD_PRICE'],
        NFT_CARD_TITLE=DISINTAR_CLASS_NAME_H1['NFT_CARD_TITLE']
    )
