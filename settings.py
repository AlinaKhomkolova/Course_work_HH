from pathlib import Path

ROOT_PATH = Path(__file__).parent
VACANCIES_JSON = ROOT_PATH.joinpath('data', 'vacancies_hh.json')
VACANCIES_TXT = ROOT_PATH.joinpath('data', 'vacancies_hh.txt')
URL = 'https://api.hh.ru/vacancies'
