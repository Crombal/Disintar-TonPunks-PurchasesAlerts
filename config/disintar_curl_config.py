import datetime
from typing import Dict

cookies: Dict[str, str] = {
    'csrftoken': '2bO3htOkdY9iqh3kyZVjFKTt25OxmJxVRCewXXnNTm1DRH5WVTy0w4EWsL7RTRWR',
}

headers: Dict[str, str] = {
    'X-Csrftoken': '2bO3htOkdY9iqh3kyZVjFKTt25OxmJxVRCewXXnNTm1DRH5WVTy0w4EWsL7RTRWR',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryG1LvLS9n9u7btjdI',
    'Referer': 'https://beta.disintar.io/collection/UQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75n1I',
}

URL: str = 'https://beta.disintar.io/api/get_entities/'


def data(page: int, limit: int) -> str:
    """
    Generate data for the post request

    :Args:
     - page: int - number of the page with NFTs
     - limit: int - limit of NFTs per page
    """
    return '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
           'Content-Disposition: form-data; name="entity_name"\r\n\r\nNFT\r\n' \
           '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
           'Content-Disposition: form-data; name="order_by"\r\n\r\n["price"]\r\n' \
           '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
           'Content-Disposition: form-data; name="filter_by"\r\n\r\n' \
           '[{"name":"collection__address","value":"UQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75n1I"}]\r\n' \
           '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
           f'Content-Disposition: form-data; name="limit"\r\n\r\n{limit}\r\n' \
           '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
           f'Content-Disposition: form-data; name="page"\r\n\r\n{page}\r\n' \
           '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
           'Content-Disposition: form-data; name="request_time"\r\n\r\n' \
           f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\r\n' \
           '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n'
