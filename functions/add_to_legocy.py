import json


def add_to_legocy(set_information: list):
    with open('set_ids.json', 'r') as json_file:
        legocy_set_dict = json.load(json_file)

    request_data_list = []

    for set_info in set_information:
        set_theme = set_info['set_theme']
        set_id = None

        for legocy_set in legocy_set_dict:
            if legocy_set['name'] == set_theme:
                set_id = legocy_set['id']
                break

        if set_id is not None:
            request_data = {
                "n_pieces": set_info['set_pieces'],
                "name": set_info['set_title'],
                "number": set_info['set_id'],
                "series_id": set_id
            }
            request_data_list.append(request_data)

        else:
            print(f"Set theme '{set_theme}' does not exist in legocy_set_dict")

    with open('request_data.json', 'w') as output_file:
        json.dump(request_data_list, output_file, indent=4)
