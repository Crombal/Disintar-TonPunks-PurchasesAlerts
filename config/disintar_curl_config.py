import datetime

cookies = {
    'csrftoken': '2bO3htOkdY9iqh3kyZVjFKTt25OxmJxVRCewXXnNTm1DRH5WVTy0w4EWsL7RTRWR',
}

headers = {
    'X-Csrftoken': '2bO3htOkdY9iqh3kyZVjFKTt25OxmJxVRCewXXnNTm1DRH5WVTy0w4EWsL7RTRWR',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryG1LvLS9n9u7btjdI',
    'Referer': 'https://beta.disintar.io/collection/UQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75n1I',
}

url = 'https://beta.disintar.io/api/get_entities/'


def data(page, limit):
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
