import pytest

from src.classes.Vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy(name='test_name', area='test_city', salary_from=100, salary_to=200, currency='test_RUB',
                   experience='Нет опыта', published_at='2024-06-17T13:01:10+0300',
                   alternate_url='https://hh.ru/vacancy/102096350')


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


def test_to_dict(vacancy):
    assert Vacancy.to_dict(vacancy) == {
        "name": "test_name",
        "area": 'test_city',
        "salary_from": 100,
        "salary_to": 200,
        "currency": 'test_RUB',
        "experience": 'Нет опыта',
        "published_at": '2024-06-17T13:01:10+0300',
        "alternate_url": 'https://hh.ru/vacancy/102096350'
    }


def test_formatting_date(vacancy):
    assert Vacancy.formatting_date(vacancy) == '17.06.2024'


def test_validate_salary(list_vacancy):
    item = list_vacancy
    assert Vacancy.validate_salary(item[0]) == 'Зарплата ОТ: 120000 ДО: 180000 RUB'
    assert Vacancy.validate_salary(item[1]) == 'Зарплата ОТ: 90000 RUB'
    assert Vacancy.validate_salary(item[2]) == 'Зарплата ДО: 250000 RUB'
    assert Vacancy.validate_salary(item[3]) == 'Уровень дохода не указан'
    assert Vacancy.validate_salary(item[4]) == 'Уровень дохода не указан'


def test_sort(list_vacancy):
    item = list_vacancy
    assert Vacancy.__lt__(item[0], item[1]) is False
    assert Vacancy.__lt__(item[1], item[0]) is True
    assert Vacancy.__gt__(item[1], item[0]) is False
    assert Vacancy.__gt__(item[0], item[1]) is True
    assert Vacancy.lt__salary(item[0], item[1]) is False
    assert Vacancy.lt__salary(item[1], item[0]) is True
    assert Vacancy.gt__salary(item[1], item[0]) is False
    assert Vacancy.gt__salary(item[0], item[1]) is True


def test_str(vacancy):
    assert Vacancy.__str__(
        vacancy) == ('Название вакансии: test_name\n'
                     'Город: test_city\n'
                     'Зарплата ОТ: 100 ДО: 200 test_RUB\n'
                     'Дата публикации: 17.06.2024\n'
                     'Ссылка на вакансию: https://hh.ru/vacancy/102096350\n'
                     'Опыт работы: Нет опыта\n')
