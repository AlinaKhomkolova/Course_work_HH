from abc import ABC, abstractmethod

import requests

from src.classes.Saver import WritingReadingData
from src.classes.Vacancy import Vacancy
from settings import URL


class BaseAPIABC(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword: str, count_page: int) -> list[object]:
        pass


class HhAPI(BaseAPIABC):
    """
     Класс для работы с API HeadHunter.
    """

    def __init__(self):
        # URL для запросов к API HeadHunter.
        self.url = URL
        # Заголовки запросов.
        self.headers = {'User-Agent': 'HH-User-Agent'}
        # Параметры запроса (текст поиска, номер страницы, количество вакансий на странице).
        self.params = {'text': '', 'page': 0, 'per_page': 10}

    def get_vacancies(self, keyword, count_page) -> list[Vacancy]:
        """Получает список вакансий по ключевому слову и количеству страниц."""
        # Установка ключевого слова для поиска вакансий.
        self.params['text'] = keyword
        job_list = self.fetch_vacancies(count_page)
        WritingReadingData().writing_data_JSON(job_list)
        return job_list

    def fetch_vacancies(self, count_page) -> list[Vacancy]:
        """Извлекает список вакансий из API и создает экземпляры Vacancy."""
        job_list = []

        for i in range(count_page):
            # Установка номера страницы.
            self.params['page'] = i
            # Выполнение запроса к API.
            response = requests.get(self.url, headers=self.headers, params=self.params)
            # Проверка статуса ответа. В случае ошибки вызовет исключение.
            response.raise_for_status()
            # Извлечение списка вакансий из ответа.
            response_json = response.json()['items']
            for item in response_json:
                vacancy = self.create_vacancy_from_item(item)
                job_list.append(vacancy)
        return job_list

    @staticmethod
    def create_vacancy_from_item(item) -> Vacancy:
        """Создает экземпляр Vacancy из элемента JSON."""
        name = item.get('name')
        area = item.get('area', {}).get('name')
        # Получение информации о зарплате.
        salary = item.get('salary')
        if salary:
            salary_from = item.get('salary', {}).get('from')
            salary_to = item.get('salary', {}).get('to')
            currency = item.get('salary', {}).get('currency')
        else:
            salary_from = None
            salary_to = None
            currency = None
        # Получение информации о требуемом опыте.
        experience_ = item.get('experience')
        if experience_:
            experience = item.get('experience', {}).get('name')
        else:
            experience = None
        published_at = item.get('published_at')
        alternate_url = item.get('alternate_url')
        # Создание экземпляра класса Vacancy.
        return Vacancy(name, area, salary_from, salary_to, currency,
                       experience, published_at, alternate_url)
