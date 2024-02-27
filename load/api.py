import json
import time

import requests

bearer_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBnb29nbGUuY29tIiwicm9sZSI6MSwiZXhwIjoxNzA5MDcwMzEyfQ.zH-5Ja-MQLom6sG8ZMJ-90t_AJjC77xfMHF5SN4lMWA'

url = 'https://api.legocy.online/api/v1/admin/sets/'

headers = {'Authorization': f'Bearer {bearer_token}'}

sets_with_ids = []

sets_failed = []


def read_data() -> list[dict]:
    with open('../static/legocy_new_sets.json', 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def make_request(set_data: dict) -> tuple[int, bool, str]:
    '''returns set id and ok (0, false) if failed'''

    set_data["number"] = int(set_data["number"])

    response = requests.post(url, json=set_data, headers=headers)

    return response.json().get("id"), response.status_code == 200, response.text


def handle_lego_set(set_data: dict):
    global sets_with_ids, sets_failed

    set_id, ok, resp_text = make_request(set_data)

    if not ok:
        sets_failed.append(
            {
                "set_data": set_data,
                "resp_text": resp_text,
            }
        )
        return

    sets_with_ids.append({**set_data, "id": set_id})


def save_results():
    global sets_with_ids, sets_failed

    with open('../static/legocy_dump_results_success.json', 'w', encoding='utf-8') as file:
        json.dump(sets_with_ids, file, ensure_ascii=False, indent=4)
    with open('../static/legocy_dump_results_errors.json', 'w', encoding='utf-8') as file:
        json.dump(sets_failed, file, ensure_ascii=False, indent=4)


def main():
    sets_data = read_data()

    for set_data in sets_data:
        print(f"Handling set: {set_data['number']}...")
        handle_lego_set(set_data)
    save_results()


if __name__ == '__main__':
    main()
