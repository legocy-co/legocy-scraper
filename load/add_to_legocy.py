import json


def add_to_legocy(set_information: list):
    with open('theme_ids.json', 'r') as json_file:
        themes_list = json.load(json_file)

    request_data_list = []

    for set_info in set_information:
        set_theme = set_info['set_theme']
        set_id = None

        for lego_theme in themes_list:
            if lego_theme['name'] == set_theme:
                set_id = lego_theme['id']
                break

        if set_id is not None:
            request_data = {
                "n_pieces": set_info['set_pieces'],
                "name": set_info['set_title'],
                "number": set_info['set_id'],
                "series_id": set_id
            }
            request_data_list.append(request_data)

    with open('request_data.json', 'w') as output_file:
        json.dump(request_data_list, output_file, indent=4)
