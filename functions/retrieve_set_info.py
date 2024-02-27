import requests
from bs4 import BeautifulSoup


def download_photos(lego_sets: list, headers) -> list:
    lego_sets_information = []

    for lego_set_info in lego_sets:
        r = requests.get(f"https://{lego_set_info['href']}", headers=headers)

        if r.status_code != 200:
            print(f'Error: {r.status_code}')
            continue

        soup = BeautifulSoup(r.text, 'html.parser')

        tables = soup.find_all("table", {"class": "themetable sortable"})
        for table in tables:
            lego_set = table.find_all("tr", {"class": "lua-brick-table-row"})

            for lego in lego_set:

                try:
                    if int(lego.find_all("td")[3].text) >= 30:
                        lego_info = {
                            "set_title": lego.find_all("td")[2].text,
                            "set_image": lego.find("a").get("href"),
                            "set_pieces": lego.find_all("td")[3].text,
                            "set_year": lego.find_all("td")[6].text[-4:]
                        }
                        lego_sets_information.append(lego_info)

                except ValueError:
                    invalid_set = {
                        "set_link": f"https://{lego_set_info['href']}",
                        "set_title": lego.find_all("td")[2].text
                    }

                    print(invalid_set)
                    continue

    return lego_sets_information