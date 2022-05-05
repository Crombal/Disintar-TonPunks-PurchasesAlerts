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
    DISINTAR_TON_PUNKS_COLLECTION_URL : str
        The Ton Punks collection url on disintar.io
    DISINTAR_LOAD_TIME : float
        Wait time of page load on disintar.io
    DISINTAR_MAX_PRICE : int
        The maximum price up to which NFTs are searched for on disintar.io
    DISINTAR_CLASS_NAME_DIV_NFT_CARD_CONTAINER : str
        The class name of nft card container div on disintar.io
    DISINTAR_CLASS_NAME_DIV_NFT_CARD_META : str
        The class name of nft card meta div on disintar.io
    DISINTAR_CLASS_NAME_DIV_NFT_CARD_PRICE : str
        The class name of nft card price div on disintar.io
    DISINTAR_CLASS_NAME_H1_NFT_CARD_TITLE : str
        The class name of nft card title h1 on disintar.io
    TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL : str
        The Ton Punks collection url on tonnft.tools
    TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL_WITH_PAGE : str
        The Ton Punks collection with page url on tonnft.tools
    TON_NFT_TOOLS_LOAD_TIME: float
        Wait time of page load on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_DIV_NFT_CARD_CONTAINER: str
        The class name of the nft card container div on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_VALUE: str
        The class name of the nft attribute value div on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_NAME: str
        The class name of the nft attribute name div on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_BUTTON_MODAL_DIALOG_CLOSE: str
        The class name of the modal dialog close button on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_LI_ATTRIBUTE_CONTAINER: str
        The class name of the li attribute container on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_LI_PAGE_ITEM: str
        The class name of the li page item on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_SPAN_ATTRIBUTE_SCORE: str
        The class name of the span attribute score on tonnft.tools
    TON_NFT_TOOLS_CLASS_NAME_UL_PAGINATION: str
        The class name of the ul pagination on tonnft.tools
    TON_NFT_TOOLS_ID_SPAN_MODAL_RARITY_RANK: str
        The id of the rarity rank for modal dialog span on tonnft.tools
    TON_NFT_TOOLS_ID_U_MODAL_RARITY_SCORE: str
        The id of the rarity score for modal dialog u on tonnft.tools
    TON_NFT_TOOLS_ID_H4_MODAL_NAME: str
        The id of the name for modal dialog h4 on tonnft.tools
    TON_NFT_TOOLS_ID_INPUT_MODAL_NFT_ADDRESS: str
        The id of the nft address for modal dialog input on tonnft.tools
    TON_NFT_TOOLS_ID_UL_MODAL_ATTRIBUTES: str
        The id of the attributes for modal dialog ul on tonnft.tools
    """

    DISINTAR_TON_PUNKS_COLLECTION_URL: str
    DISINTAR_LOAD_TIME: float
    DISINTAR_MAX_PRICE: int
    DISINTAR_CLASS_NAME_DIV_NFT_CARD_CONTAINER: str
    DISINTAR_CLASS_NAME_DIV_NFT_CARD_META: str
    DISINTAR_CLASS_NAME_DIV_NFT_CARD_PRICE: str
    DISINTAR_CLASS_NAME_H1_NFT_CARD_TITLE: str
    TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL: str
    TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL_WITH_PAGE: str
    TON_NFT_TOOLS_LOAD_TIME: float
    TON_NFT_TOOLS_CLASS_NAME_DIV_NFT_CARD_CONTAINER: str
    TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_VALUE: str
    TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_NAME: str
    TON_NFT_TOOLS_CLASS_NAME_BUTTON_MODAL_DIALOG_CLOSE: str
    TON_NFT_TOOLS_CLASS_NAME_LI_ATTRIBUTE_CONTAINER: str
    TON_NFT_TOOLS_CLASS_NAME_LI_PAGE_ITEM: str
    TON_NFT_TOOLS_CLASS_NAME_SPAN_ATTRIBUTE_SCORE: str
    TON_NFT_TOOLS_CLASS_NAME_UL_PAGINATION: str
    TON_NFT_TOOLS_ID_SPAN_MODAL_RARITY_RANK: str
    TON_NFT_TOOLS_ID_U_MODAL_RARITY_SCORE: str
    TON_NFT_TOOLS_ID_H4_MODAL_NAME: str
    TON_NFT_TOOLS_ID_INPUT_MODAL_NFT_ADDRESS: str
    TON_NFT_TOOLS_ID_UL_MODAL_ATTRIBUTES: str

    def __str__(self) -> str:
        """This method returns the string representation of the Config"""
        return (
            f'DISINTAR_TON_PUNKS_COLLECTION_URL: {self.DISINTAR_TON_PUNKS_COLLECTION_URL}\n'
            f'DISINTAR_LOAD_TIME: {self.DISINTAR_LOAD_TIME}\n'
            f'DISINTAR_MAX_PRICE: {self.DISINTAR_MAX_PRICE}\n'
            f'DISINTAR_CLASS_NAME_DIV_NFT_CARD_CONTAINER: {self.DISINTAR_CLASS_NAME_DIV_NFT_CARD_CONTAINER}\n'
            f'DISINTAR_CLASS_NAME_DIV_NFT_CARD_META: {self.DISINTAR_CLASS_NAME_DIV_NFT_CARD_META}\n'
            f'DISINTAR_CLASS_NAME_DIV_NFT_CARD_PRICE: {self.DISINTAR_CLASS_NAME_DIV_NFT_CARD_PRICE}\n'
            f'DISINTAR_CLASS_NAME_H1_NFT_CARD_TITLE: {self.DISINTAR_CLASS_NAME_H1_NFT_CARD_TITLE}\n'
            f'TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL: {self.TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL}\n'
            f'TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL_WITH_PAGE: '
            f'{self.TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL_WITH_PAGE}\n'
            f'TON_NFT_TOOLS_LOAD_TIME: {self.TON_NFT_TOOLS_LOAD_TIME}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_DIV_NFT_CARD_CONTAINER: {self.TON_NFT_TOOLS_CLASS_NAME_DIV_NFT_CARD_CONTAINER}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_VALUE: {self.TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_VALUE}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_NAME: {self.TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_NAME}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_BUTTON_MODAL_DIALOG_CLOSE: '
            f'{self.TON_NFT_TOOLS_CLASS_NAME_BUTTON_MODAL_DIALOG_CLOSE}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_LI_ATTRIBUTE_CONTAINER: {self.TON_NFT_TOOLS_CLASS_NAME_LI_ATTRIBUTE_CONTAINER}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_LI_PAGE_ITEM: {self.TON_NFT_TOOLS_CLASS_NAME_LI_PAGE_ITEM}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_SPAN_ATTRIBUTE_SCORE: {self.TON_NFT_TOOLS_CLASS_NAME_SPAN_ATTRIBUTE_SCORE}\n'
            f'TON_NFT_TOOLS_CLASS_NAME_UL_PAGINATION: {self.TON_NFT_TOOLS_CLASS_NAME_UL_PAGINATION}\n'
            f'TON_NFT_TOOLS_ID_SPAN_MODAL_RARITY_RANK: {self.TON_NFT_TOOLS_ID_SPAN_MODAL_RARITY_RANK}\n'
            f'TON_NFT_TOOLS_ID_U_MODAL_RARITY_SCORE: {self.TON_NFT_TOOLS_ID_U_MODAL_RARITY_SCORE}\n'
            f'TON_NFT_TOOLS_ID_H4_MODAL_NAME: {self.TON_NFT_TOOLS_ID_H4_MODAL_NAME}\n'
            f'TON_NFT_TOOLS_ID_INPUT_MODAL_NFT_ADDRESS: {self.TON_NFT_TOOLS_ID_INPUT_MODAL_NFT_ADDRESS}\n'
            f'TON_NFT_TOOLS_ID_UL_MODAL_ATTRIBUTES: {self.TON_NFT_TOOLS_ID_UL_MODAL_ATTRIBUTES}'
        )


def _load_config() -> Config:
    """Load config values from config file and pass them to the Config"""
    config = yaml.safe_load(open("config.yaml"))

    DISINTAR = config['DISINTAR']
    DISINTAR_CLASS_NAME = DISINTAR['CLASS_NAME']
    DISINTAR_CLASS_NAME_DIV = DISINTAR_CLASS_NAME['DIV']
    DISINTAR_CLASS_NAME_H1 = DISINTAR_CLASS_NAME['H1']
    TON_NFT_TOOLS = config['TON_NFT_TOOLS']
    TON_NFT_TOOLS_CLASS_NAME = TON_NFT_TOOLS['CLASS_NAME']
    TON_NFT_TOOLS_CLASS_NAME_DIV = TON_NFT_TOOLS_CLASS_NAME['DIV']
    TON_NFT_TOOLS_CLASS_NAME_BUTTON = TON_NFT_TOOLS_CLASS_NAME['BUTTON']
    TON_NFT_TOOLS_CLASS_NAME_LI = TON_NFT_TOOLS_CLASS_NAME['LI']
    TON_NFT_TOOLS_CLASS_NAME_SPAN = TON_NFT_TOOLS_CLASS_NAME['SPAN']
    TON_NFT_TOOLS_CLASS_NAME_UL = TON_NFT_TOOLS_CLASS_NAME['UL']
    TON_NFT_TOOLS_ID = TON_NFT_TOOLS['ID']
    TON_NFT_TOOLS_ID_SPAN = TON_NFT_TOOLS_ID['SPAN']
    TON_NFT_TOOLS_ID_U = TON_NFT_TOOLS_ID['U']
    TON_NFT_TOOLS_ID_H4 = TON_NFT_TOOLS_ID['H4']
    TON_NFT_TOOLS_ID_INPUT = TON_NFT_TOOLS_ID['INPUT']
    TON_NFT_TOOLS_ID_UL = TON_NFT_TOOLS_ID['UL']

    loaded_config = Config(
        DISINTAR_TON_PUNKS_COLLECTION_URL=DISINTAR['TON_PUNKS_COLLECTION_URL'],
        DISINTAR_LOAD_TIME=DISINTAR['LOAD_TIME'],
        DISINTAR_MAX_PRICE=DISINTAR['MAX_PRICE'],
        DISINTAR_CLASS_NAME_DIV_NFT_CARD_CONTAINER=DISINTAR_CLASS_NAME_DIV['NFT_CARD_CONTAINER'],
        DISINTAR_CLASS_NAME_DIV_NFT_CARD_META=DISINTAR_CLASS_NAME_DIV['NFT_CARD_META'],
        DISINTAR_CLASS_NAME_DIV_NFT_CARD_PRICE=DISINTAR_CLASS_NAME_DIV['NFT_CARD_PRICE'],
        DISINTAR_CLASS_NAME_H1_NFT_CARD_TITLE=DISINTAR_CLASS_NAME_H1['NFT_CARD_TITLE'],
        TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL=TON_NFT_TOOLS['TON_PUNKS_COLLECTION_URL'],
        TON_NFT_TOOLS_TON_PUNKS_COLLECTION_URL_WITH_PAGE=TON_NFT_TOOLS['TON_PUNKS_COLLECTION_URL_WITH_PAGE'],
        TON_NFT_TOOLS_LOAD_TIME=TON_NFT_TOOLS['LOAD_TIME'],
        TON_NFT_TOOLS_CLASS_NAME_DIV_NFT_CARD_CONTAINER=TON_NFT_TOOLS_CLASS_NAME_DIV['NFT_CARD_CONTAINER'],
        TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_VALUE=TON_NFT_TOOLS_CLASS_NAME_DIV['ATTRIBUTE_VALUE'],
        TON_NFT_TOOLS_CLASS_NAME_DIV_ATTRIBUTE_NAME=TON_NFT_TOOLS_CLASS_NAME_DIV['ATTRIBUTE_NAME'],
        TON_NFT_TOOLS_CLASS_NAME_BUTTON_MODAL_DIALOG_CLOSE=TON_NFT_TOOLS_CLASS_NAME_BUTTON['MODAL_DIALOG_CLOSE'],
        TON_NFT_TOOLS_CLASS_NAME_LI_ATTRIBUTE_CONTAINER=TON_NFT_TOOLS_CLASS_NAME_LI['ATTRIBUTE_CONTAINER'],
        TON_NFT_TOOLS_CLASS_NAME_LI_PAGE_ITEM=TON_NFT_TOOLS_CLASS_NAME_LI['PAGE_ITEM'],
        TON_NFT_TOOLS_CLASS_NAME_SPAN_ATTRIBUTE_SCORE=TON_NFT_TOOLS_CLASS_NAME_SPAN['ATTRIBUTE_SCORE'],
        TON_NFT_TOOLS_CLASS_NAME_UL_PAGINATION=TON_NFT_TOOLS_CLASS_NAME_UL['PAGINATION'],
        TON_NFT_TOOLS_ID_SPAN_MODAL_RARITY_RANK=TON_NFT_TOOLS_ID_SPAN['MODAL_RARITY_RANK'],
        TON_NFT_TOOLS_ID_U_MODAL_RARITY_SCORE=TON_NFT_TOOLS_ID_U['MODAL_RARITY_SCORE'],
        TON_NFT_TOOLS_ID_H4_MODAL_NAME=TON_NFT_TOOLS_ID_H4['MODAL_NAME'],
        TON_NFT_TOOLS_ID_INPUT_MODAL_NFT_ADDRESS=TON_NFT_TOOLS_ID_INPUT['MODAL_NFT_ADDRESS'],
        TON_NFT_TOOLS_ID_UL_MODAL_ATTRIBUTES=TON_NFT_TOOLS_ID_UL['MODAL_ATTRIBUTES']
    )

    logger.info(f'Successfully loaded config:\n{loaded_config}')
    return loaded_config
