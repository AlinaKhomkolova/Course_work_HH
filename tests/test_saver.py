import json
import os.path

import pytest

from src.classes.Saver import WritingReadingData
from src.classes.Vacancy import Vacancy


@pytest.fixture
def list_vacancy():
    return [
        Vacancy(name='Software Engineer', area='Москва', salary_from=120000, salary_to=180000, currency='RUB',
                experience='От 3 до 6 лет', published_at='2024-06-23T10:00:00+0300',
                alternate_url='https://hh.ru/vacancy/100001'),
        Vacancy(name='Data Analyst', area='Питер', salary_from=90000, salary_to=None, currency='RUB',
                experience='От 1 до 3 лет', published_at='2024-06-22T15:30:00+0300',
                alternate_url='https://hh.ru/vacancy/100002'),
        Vacancy(name='Project Manager', area='Новосибирск', salary_from=None, salary_to=250000, currency='RUB',
                experience='От 5 лет', published_at='2024-06-21T09:45:00+0300',
                alternate_url='https://hh.ru/vacancy/100003'),
        Vacancy(name='UX/UI Designer', area='Казань', salary_from=None, salary_to=None, currency='RUB',
                experience='От 2 до 4 лет', published_at='2024-06-20T14:20:00+0300',
                alternate_url='https://hh.ru/vacancy/100004'),
        Vacancy(name='Customer Support Specialist', area='Екатеринбург', salary_from=None, salary_to=None,
                currency='USD',
                experience='Нет опыта', published_at='2024-06-19T11:10:00+0300',
                alternate_url='https://hh.ru/vacancy/100005')
    ]


@pytest.fixture
def setup_test_file(tmp_path):
    # Временный файл для тестирования
    test_file = tmp_path / "test_vacancies.json"
    test_file.touch()
    return str(test_file)


@pytest.fixture
def setup_test_file_txt(tmp_path):
    # Временный файл для тестирования
    test_file = tmp_path / "test_vacancies.txt"
    test_file.touch()
    return str(test_file)


def test_writing_data_JSON(setup_test_file, list_vacancy):
    test_path = setup_test_file

    WritingReadingData().writing_data_JSON(list_vacancy, path=test_path)

    with open(test_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert isinstance(saved_data, list)
    assert len(saved_data) == len(list_vacancy)

    for item in saved_data:
        assert isinstance(item, dict)

    assert saved_data[0]['name'] == 'Software Engineer'
    assert saved_data[2]['area'] == 'Новосибирск'
    assert saved_data[3]['salary_from'] is None
    assert saved_data[1]['salary_to'] is None


def test_writing_data_txt(setup_test_file_txt, list_vacancy):
    test_path = setup_test_file_txt

    WritingReadingData().writing_data_txt(list_vacancy, test_path)

    assert os.path.exists(test_path)
    assert os.path.getsize(test_path) > 0




