import json
from datetime import datetime

import requests

from settings import URL, VACANCIES, VACANCIES_TXT
from src.abstracted_classes import HhAPIData, JSONSaver


class Vacancy:
    """
    Класс для представления вакансии.
     Args:
            name (str): Название вакансии.
            area (str): Город, в котором расположена вакансия.
            salary_from (int or None): Минимальная зарплата.
            salary_to (int or None): Максимальная зарплата.
            currency (str or None): Валюта зарплаты.
            experience (str or None): Требуемый опыт работы.
            published_at (str): Дата публикации вакансии в формате ISO 8601.
            alternate_url (str): Ссылка на вакансию.
            """

    def __init__(self, name, area, salary_from, salary_to, currency,
                 experience, published_at, alternate_url):
        self.__name = name
        self.__area = area
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__currency = currency
        self.__experience = experience
        self.__published_at = published_at
        self.__alternate_url = alternate_url

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    def to_dict(self):
        """Преобразует объект в словарь."""
        return {
            "name": self.__name,
            "area": self.__area,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "currency": self.__currency,
            "experience": self.__experience,
            "published_at": self.__published_at,
            "alternate_url": self.__alternate_url
        }

    def formatting_date(self) -> str:
        """Форматирует дату публикации вакансии."""
        date = datetime.strptime(self.__published_at, '%Y-%m-%dT%H:%M:%S%z')
        return f'{date:%d.%m.%Y}'

    def validate_salary(self) -> str:
        """Проверяет и форматирует данные о зарплате."""
        if self.__salary_from is not None and self.__salary_to is not None:
            return f"Зарплата ОТ: {self.__salary_from} ДО: {self.__salary_to} {self.__currency}"
        elif self.__salary_from is None and self.__salary_to is not None:
            return f"Зарплата ДО: {self.__salary_to} {self.__currency}"
        elif self.__salary_from is not None and self.__salary_to is None:
            return f"Зарплата ОТ: {self.__salary_from} {self.__currency}"
        else:
            return "Уровень дохода не указан"

    def __lt__date(self, other):
        """Определяет оператор '<' для сравнения по дате публикации."""
        return self.__published_at < other.__published_at

    def __gt__date(self, other):
        """Определяет оператор '>' для сравнения по дате публикации."""
        return self.__published_at > other.__published_at

    def __lt__salary(self, other):
        """Определяет оператор '<' для сравнения по зарплате."""
        if self.__salary_from is None:
            return False
        if other.__salary_from is None:
            return True
        return self.__salary_from < other.__salary_from

    def __gt__salary(self, other):
        """Определяет оператор '>' для сравнения по зарплате."""
        if self.__salary_from is None:
            return True
        if other.__salary_from is None:
            return False
        return self.__salary_from > other.__salary_from

    def __str__(self):
        """Возвращает строковое представление объекта Vacancy."""
        return (f"Название вакансии: {self.__name}\n"
                f"Город: {self.__area}\n"
                f"{self.validate_salary()}\n"
                f"Дата публикации: {self.formatting_date()}\n"
                f"Ссылка на вакансию: {self.__alternate_url}\n"
                f"Опыт работы: {self.__experience}\n")


class HhAPI(HhAPIData):
    """
     Класс для работы с API HeadHunter.
    """

    def __init__(self):
        """
        url (str): URL для запросов к API HeadHunter.
        headers (dict): Заголовки запросов.
        params (dict): Параметры запроса (текст поиска, номер страницы, количество вакансий на странице).
        """

        self.url = URL
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, keyword, count_page) -> list[Vacancy]:
        """Получает список вакансий по ключевому слову и количеству страниц."""
        self.params['text'] = keyword
        job_list = []
        for i in range(count_page):
            self.params['page'] = count_page
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()
            response_json = response.json()['items']
            for item in response_json:
                name = item.get('name')
                area = item.get('area', {}).get('name')

                salary = item.get('salary')
                if salary:
                    salary_from = item.get('salary', {}).get('from')
                    salary_to = item.get('salary', {}).get('to')
                    currency = item.get('salary', {}).get('currency')
                else:
                    salary_from = None
                    salary_to = None
                    currency = None

                experience_ = item.get('experience')
                if experience_:
                    experience = item.get('experience', {}).get('name')
                else:
                    experience = None
                published_at = item.get('published_at')
                alternate_url = item.get('alternate_url')
                vacancy = Vacancy(name, area, salary_from, salary_to, currency,
                                  experience, published_at, alternate_url)
                job_list.append(vacancy)
        return job_list


class WritingReadingData(Vacancy, JSONSaver):
    def save_to_file(self, path: str = VACANCIES_TXT):
        """Сохраняет информацию о вакансии в файл."""
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f"Название вакансии: {self.__name}\n"
                       f"Город: {self.__area}\n"
                       f"{self.validate_salary()}\n"
                       f"Дата публикации: {self.formatting_date()}\n"
                       f"Ссылка на вакансию: {self.__alternate_url}\n"
                       f"Опыт работы: {self.__experience}\n\n")

    def read_data(self, path: str = VACANCIES):
        """
        Читает данные из файла.
        Args:
            path (str): Путь к файлу с данными.
        Returns:
            list: Список данных из файла."""
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)

    def writing_data(self, data: list, path: str = VACANCIES):
        """
        Записывает данные в файл.
        Args:
            data (list): Список данных для записи.
            path (str): Путь к файлу для записи.
        Returns:
            list: Список данных, которые были записаны в файл.
            """
        with open(path, "w", encoding="utf-8") as file:
            json.dump([vacancy.to_dict() for vacancy in data], file, ensure_ascii=False, indent=4)
        return data
