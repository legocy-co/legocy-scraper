import requests
from bs4 import BeautifulSoup


def get_theme_pieces_by_name(theme: str) -> int:

    popular_themes = (
        "DC SuperHeroes",
        "Architecture",
        "Batman",
        "BrickHeadz",
        "Creator",
        "Creator Expert",
        "DC Comics Super Heroes",
        "Icons",
        "Ideas",
        "Marvel Super Heroes",
        "Minecraft",
        "Ninjago",
        "Overwatch",
        "Star Wars",
        "Super Mario",
        "Technic",
        "The Hobbit",
        "The LEGO Batman Movie",
        "Harry Potter",
    )

    if theme in popular_themes:
        return 30

    return 100


def filter_sets(lego_sets: list, headers) -> list:

    error_requests = 0
    error_parsing = 0

    lego_sets_information = []

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

                try:
                    theme = soup.find("span", {"class": "mw-page-title-main"}).text
                    if theme.endswith(" (Theme)"):
                            theme = theme[:-8]
                    if theme == "LEGO Ideas":
                        theme = "Ideas"
                    if theme == "Marvel":
                        theme = "Marvel Super Heroes"
                    if theme == "LEGO Dimensions":
                        theme = "Dimensions"

                    set_pieces = int(lego.find_all("td")[3].text)
                    
                    theme_min_pieces = get_theme_pieces_by_name(theme)
                    
                    if set_pieces < theme_min_pieces:
                        print(f"Not enough pieces for theme {theme}. Want {theme_min_pieces} have {set_pieces}")
                        continue
                        
                    lego_info = {
                        "set_title": lego.find_all("td")[2].text,
                        "set_id": lego.find_all("td")[1].text,
                        "set_theme": theme,
                        "set_image": lego.find("a").get("href"),
                        "set_pieces": set_pieces,
                        "set_year": lego.find_all("td")[6].text[-4:]
                    }
                    lego_sets_information.append(lego_info)
                
                except ValueError:
                    invalid_set = {
                        "invalid_set_link": f"https://{lego_set_info['href']}",
                        "set_title": lego.find_all("td")[2].text
                    }

                    print(invalid_set)
                    error_parsing += 1
                    continue

    print(f"Errors Count: {error_requests} requests, {error_parsing} parsing")

    return lego_sets_information
