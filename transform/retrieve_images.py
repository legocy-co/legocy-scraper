import json

import requests
from bs4 import BeautifulSoup


def get_legocy_ids() -> list:
    with open("static/legocy_go_public_lego_sets.json", 'r') as file:
        lego_ids = []
        legocy_sets = json.loads(file.read())

        for set in legocy_sets:
            lego_ids.append(set["number"])

        return lego_ids


def retrieve_images(lego_sets: list, headers) -> list:
    error_requests = 0
    error_parsing = 0

    lego_set_images = []

    legocy_set_ids = get_legocy_ids()

    for lego_set_info in lego_sets:
        r = requests.get(f"https://{lego_set_info['href']}", headers=headers)

        if r.status_code != 200:
            print(f'Error: {r.status_code}')
            error_requests += 1
            continue

        soup = BeautifulSoup(r.text, 'html.parser')
        tables = soup.find_all("table", {"class": "themetable sortable"})

        for table in tables:
            lego_set = table.find_all("tr", {"class": "lua-brick-table-row"})

            for lego in lego_set:
                if lego.find_all("td")[1].text in str(legocy_set_ids):
                    lego_info = {
                        "set_id": lego.find_all("td")[1].text,
                        "set_image": lego.find("a").get("href"),
                    }

                    lego_set_images.append(lego_info)

    print(f"Errors Count: {error_requests} requests, {error_parsing} parsing")
    return lego_set_images
