from load.add_to_legocy import add_to_legocy as load
from load.download_images import download_images
from transform.retrieve_images import retrieve_images
from transform.sets_list_filtered import filter_sets as transform
from extract.sets_list_raw import retrieve_links as extract

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

if __name__ == '__main__':
    '''
    load(
        transform(
            extract(
                headers
            ),
            headers
        )
    )
    '''

    download_images(retrieve_images(extract(headers), headers), headers)