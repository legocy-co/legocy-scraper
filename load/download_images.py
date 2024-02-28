import os

import requests


def download_images(lego_images: list[dict], headers):

    errors = []

    if not os.path.exists('lego_images'):
        os.makedirs('lego_images')

    for lego_set in lego_images:
        number = str(lego_set['set_id'])
        url = lego_set['set_image']

        folder_path = os.path.join('lego_images', number)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        filename = os.path.basename(url)

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                with open(os.path.join(folder_path, f"{filename}.png"), 'wb') as f:
                    f.write(response.content)
                    print(f"Downloaded {filename} to {folder_path}")
            else:
                print(f"Failed to download {filename} from {url}")

        except requests.exceptions.MissingSchema as f:
            errors.append(f)

    with open('errors/download_images_error.txt', 'w') as output_file:
        for error in errors:
            output_file.write(error + "\n")
