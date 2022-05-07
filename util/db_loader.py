# !/usr/bin/env python
"""Script for loading TON PUNKS information from json DB"""

import sys
import json

from typing import List
from loguru import logger
from pydantic import BaseModel
from util.time_measure_decorator import timeit

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')


class TonPunk(BaseModel):
    """
    A class to represent a Ton Punk NFT.

    ...

    Attributes
    ----------
    name : str
        name of the TON PUNK
    address : str
        address of the TON PUNK
    rarity_score : float
        rarity score of the TON PUNK
    rating_rank : int
        rating rank of the TON PUNK
    """

    name: str
    address: str
    rarity_score: float
    rating_rank: int


@timeit
def load_db() -> List[TonPunk]:
    """
    Load TON PUNKS information from json DB

    :Returns:
     - List[TonPunk] - Count of pages with NFTs
    """
    TON_PUNKS_DB: List[TonPunk] = []
    db_data = json.load(open('punks_db.json', 'r'))
    for punk in db_data:
        TON_PUNKS_DB.append(TonPunk(
            name=punk['name'],
            address=punk['address'],
            rarity_score=punk['rarity_score'],
            rating_rank=punk['rating_rank']
        ))
    logger.info(f'Successfully loaded json DB. Count of the TON PUNKS: {len(TON_PUNKS_DB)}')
    return TON_PUNKS_DB
