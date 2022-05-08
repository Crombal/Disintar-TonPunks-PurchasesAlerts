import datetime
import requests

from typing import Dict


class DisintarCurlConfigs:
    """
    A class to represent the curl configs for disintar.io
    """

    def __init__(self, cookies: Dict[str, str], headers: Dict[str, str]):
        self.COUNT_OF_PAGES: int = 256
        self.NFTS_LIMIT_PER_PAGE: int = 21
        self.API_URL: str = 'https://beta.disintar.io/api/get_entities/'
        self.__TON_PUNKS_COLLECTION_ADDRESS: str = 'UQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75n1I'
        self.__TON_PUNKS_URL: str = f'https://beta.disintar.io/collection/{self.__TON_PUNKS_COLLECTION_ADDRESS}'
        self.__BOUNDARY: Dict[str, str] = {
            'key': 'boundary',
            'value': '--boundary\r\n'
        }
        self.cookies: Dict[str, str] = cookies
        self.headers: Dict[str, str] = headers
        self.reset_csrf()

    def __get_csrf(self) -> str:
        """
        Get valid crsf token
        """

        return requests.get(url=self.__TON_PUNKS_URL).headers['set-cookie'].split(';')[0].split('=')[1]

    def reset_csrf(self) -> None:
        """
        Reset csrf token for cookies and headers
        """

        csrf = self.__get_csrf()

        self.cookies = {
            'csrftoken': csrf,
        }

        self.headers = {
            'X-Csrftoken': csrf,
            f'Content-Type': f'multipart/form-data; boundary={self.__BOUNDARY["key"]}',
            'Referer': self.__TON_PUNKS_URL,
        }

    def data(self, page: int) -> str:
        return f'{self.__BOUNDARY["value"]}' \
               'Content-Disposition: form-data; name="entity_name"\r\n\r\nNFT\r\n' \
               f'{self.__BOUNDARY["value"]}' \
               'Content-Disposition: form-data; name="order_by"\r\n\r\n["price"]\r\n' \
               f'{self.__BOUNDARY["value"]}' \
               'Content-Disposition: form-data; name="filter_by"\r\n\r\n' \
               '[{' \
               '"name":"collection__address",' \
               f'"value":"{self.__TON_PUNKS_COLLECTION_ADDRESS}"' \
               '}]\r\n' \
               f'{self.__BOUNDARY["value"]}' \
               f'Content-Disposition: form-data; name="limit"\r\n\r\n{self.NFTS_LIMIT_PER_PAGE}\r\n' \
               f'{self.__BOUNDARY["value"]}' \
               f'Content-Disposition: form-data; name="page"\r\n\r\n{page}\r\n' \
               f'{self.__BOUNDARY["value"]}' \
               'Content-Disposition: form-data; name="request_time"\r\n\r\n' \
               f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\r\n'
