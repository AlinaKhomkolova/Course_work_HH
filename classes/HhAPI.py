import requests

from classes.ABC_classes import BaseAPI
from classes.Saver import WritingReadingData
from classes.Vacancy import Vacancy
from settings import URL, VACANCIES_JSON


class HhAPI(BaseAPI):
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
        job_list = []

        for i in range(count_page):
            # Установка номера страницы.
            self.params['page'] = count_page
            # Выполнение запроса к API.
            response = requests.get(self.url, headers=self.headers, params=self.params)
            # Проверка статуса ответа. В случае ошибки вызовет исключение.
            response.raise_for_status()
            # Извлечение списка вакансий из ответа.
            response_json = response.json()['items']

            for item in response_json:
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
                vacancy = Vacancy(name, area, salary_from, salary_to, currency,
                                  experience, published_at, alternate_url)
                job_list.append(vacancy)

        # Запись полученных данных в файл JSON.
        WritingReadingData().writing_data_JSON(job_list)

        return job_list
