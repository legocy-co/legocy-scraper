from load.add_to_legocy import add_to_legocy
from transform.sets_list_filtered import download_photos
from extract.sets_list_raw import retrieve_links

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

if __name__ == '__main__':
    list_of_sets = retrieve_links(headers)
    set_information = download_photos(list_of_sets, headers)
    add_to_legocy(set_information)
