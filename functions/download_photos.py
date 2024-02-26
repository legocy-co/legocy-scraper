import os
import re
import requests
from bs4 import BeautifulSoup


def download_photos(urls: dict, headers):
    for key in urls.keys():
        for sets in urls[key]:
                r = requests.get(sets["url"], headers=headers)

                if r.status_code != 200:
                    print(f'Error: {r.status_code}')
                    continue

                soup = BeautifulSoup(r.text, 'html.parser')

                # Find all script tags
                script_tags = soup.find_all('script')

                # Extract the contents of each script tag
                for script in script_tags:
                    print(script)


