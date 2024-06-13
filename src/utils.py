import json

import requests

from settings import VACANCIES, URL


def write_data_to_file(url: str = URL, path: str = VACANCIES) -> list[dict]:
    """Запись данных в файл"""
    with open(path, "w", encoding="utf-8") as file:
        json_data = requests.get(url).json()
        json.dump(json_data, file, ensure_ascii=False, indent=4)
    return json_data



