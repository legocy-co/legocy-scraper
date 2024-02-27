from functions.retrieve_set_info import download_photos
from functions.retireve_links import retrieve_links

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

if __name__ == '__main__':
    list_of_sets = retrieve_links(headers)
    download_photos(list_of_sets, headers)
