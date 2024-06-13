from pathlib import Path

ROOT_PATH = Path(__file__).parent
VACANCIES = ROOT_PATH.joinpath('data', 'vacancies_hh.json')
URL = 'https://api.hh.ru/vacancies'
