from functions.download_photos import download_photos
from functions.retireve_links import retrieve_links

min_year = 2010
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

if __name__ == '__main__':
    dict_of_urls = retrieve_links(headers, min_year)
    print(dict_of_urls)
    download_photos(dict_of_urls, headers)
