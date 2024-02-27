import json

with open("../static/request_data.json", "r") as file:
    scraped_data_list = json.load(file)

with open("../static/legocy_go_public_lego_sets.json", "r") as second_file:
    legocy_dict = json.load(second_file)

exist_legocy_numbers = set(
    [
        _set["number"]
        for _set in legocy_dict
    ]
)

print(len(legocy_dict))

with open("../static/legocy_new_sets.json", 'w', encoding='utf-8') as f:
        f.write(
            json.dumps(
                [
                    _parsed_set for _parsed_set in
                    scraped_data_list if int(_parsed_set["number"]) not in exist_legocy_numbers
                ],
                indent=4
            )
        )

