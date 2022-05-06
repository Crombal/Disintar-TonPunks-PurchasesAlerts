import json
import time
import asyncio
import aiohttp
import requests
import datetime

cookies = {
    'csrftoken': '2bO3htOkdY9iqh3kyZVjFKTt25OxmJxVRCewXXnNTm1DRH5WVTy0w4EWsL7RTRWR',
}

headers = {
    'X-Csrftoken': '2bO3htOkdY9iqh3kyZVjFKTt25OxmJxVRCewXXnNTm1DRH5WVTy0w4EWsL7RTRWR',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryG1LvLS9n9u7btjdI',
    'Referer': 'https://beta.disintar.io/collection/UQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75n1I',
}

FULL_NFTS_DB = []
start_time = time.time()


async def gather_data(pages_count, limit):
    await asyncio.gather(*[load_page_content(page, limit) for page in range(pages_count)])


async def load_page_content(page, limit):
    data = '------WebKitFormBoundaryG1LvLS9n9u7btjdI\r\n' \
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

    async with aiohttp.ClientSession() as session:
        response = await session.post(url='https://beta.disintar.io/api/get_entities/', cookies=cookies,
                                      headers=headers, data=data)
        await parse_nfts(await response.json())


async def parse_nfts(json_response):
    await asyncio.gather(*[parse_nft(nft) for nft in json_response['data']])


async def parse_nft(nft):
    FULL_NFTS_DB.append({
        'name': nft['name'],
        'price': nft['price'],
        'address': nft['address'],
        'owner': nft['owner']['wallet_address'],
        'is_selling': nft['is_selling']
    })


def main():
    asyncio.run(gather_data(256, 21))
    finish_time = time.time() - start_time
    print(len(FULL_NFTS_DB))
    print(f"Затраченное на работу скрипта время: {finish_time}")


if __name__ == "__main__":
    main()
