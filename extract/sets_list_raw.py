import requests
from bs4 import BeautifulSoup


def retrieve_links(headers) -> list[dict]:
    lego_sets_list = []

    url = f'https://brickipedia.fandom.com/wiki/LEGO_Wiki'

    re = requests.get(url, headers=headers)

    if re.status_code != 200:
        print(f'Error: {re.status_code}')
        return

    soup = BeautifulSoup(re.text, 'html.parser')
    lego_set_themes = soup.find_all("table", {"cellspacing": "8"})

    if not lego_set_themes:
        print("No lego sets found, please check code")
        return

    for table in lego_set_themes:
        for lego_sets in table.find_all("table", "characterportal"):

            lego_set = lego_sets.select("div[style='position:relative; height: 90px; width: 100px;']")

            for div in lego_set:

                link = div.find("div",
                                style="position: absolute; top: 0px; left: 0px; font-size: 130px; overflow: hidden; line-height: 100px; z-index: 3")
                a_tag = link.find("a")

                if a_tag:
                    href = a_tag.get("href")
                    title = a_tag.get("title")

                    lego_info = {
                        "title": title,
                        "href": f"brickipedia.fandom.com{href}"
                    }

                    lego_sets_list.append(lego_info)

    lego_sets_list.append({
            "title": "Super Heroes",
            "href": "brickipedia.fandom.com/wiki/Super_Heroes"
        })
    return lego_sets_list
