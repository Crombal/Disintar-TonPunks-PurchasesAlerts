# !/usr/bin/env python
"""Script for initialize a web driver"""

import sys

from loguru import logger
from typing import Any
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from fake_useragent import UserAgent  # type: ignore
from webdriver_manager.firefox import GeckoDriverManager  # type: ignore

logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')


class _FirefoxOptions(BaseModel):
    """
    A class to represent the options for the Firefox web driver.

    ...

    Attributes
    ----------
    options : webdriver.FirefoxOptions
        The options for the Firefox web driver
    """

    options: Any


class FirefoxDriver(BaseModel):
    """
    A class to represent a Firefox web driver.

    ...

    Attributes
    ----------
    driver : webdriver.Firefox
        The Firefox webdriver
    """

    driver: Any


def __load_options() -> _FirefoxOptions:
    """Load options to the Firefox web driver"""
    firefox_options = _FirefoxOptions(options=webdriver.FirefoxOptions())
    firefox_options.options.set_preference('general.useragent.override', UserAgent().random)  # user-agent
    firefox_options.options.set_preference('dom.webdriver.enabled', False)  # disable webdriver mode
    firefox_options.options.headless = True  # headless mode
    logger.info('Successfully loaded options for the Firefox webdriver')
    return firefox_options


def _load_driver() -> FirefoxDriver:
    """Set options to the Firefox web driver and load it"""
    service = Service(GeckoDriverManager().install())
    options = __load_options().options
    firefox_driver = FirefoxDriver(driver=webdriver.Firefox(service=service, options=options))
    logger.info('Successfully loaded Firefox webdriver with options')
    return firefox_driver
