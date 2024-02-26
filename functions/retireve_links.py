from datetime import datetime

import requests
from bs4 import BeautifulSoup


def retrieve_links(headers, min_year) -> {}:
    lego_dict = {}

    for year in range(min_year, datetime.now().year):

        lego_dict[year] = []

        url = f'https://www.bricklink.com/catalogList.asp?q=&catType=S&catID=&itemYear={year}'

        re = requests.get(url, headers=headers)

        if re.status_code != 200:
            print(f'Error: {re.status_code}')
            continue

        soup = BeautifulSoup(re.text, 'html.parser')
        div_container = soup.find('table',
                                  class_='bg-color--white catalog-list__body-main catalog-list__body-main--alternate-row')
        if not div_container:
            continue

        lego_sets = div_container.find_all("tr")

        for fv_element in lego_sets:
            item_id_element = fv_element.find("a")

            if not item_id_element:
                continue

            general_info = fv_element.find_all("td")[2]
            set_information = general_info.find("font")

            try:
                part_count = int(set_information.text.split(",")[0][:-5])
            except ValueError:
                continue

            if part_count <= 100:
                continue

            sets = {
                'item_id': item_id_element.text,
                'url': f"https://www.bricklink.com{item_id_element.attrs['href']}"
            }

            lego_dict[year].append(sets)

            print(f"Saving Lego Set ID: {sets['item_id']}...")

    return lego_dict

