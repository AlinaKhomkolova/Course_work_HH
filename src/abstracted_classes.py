from abc import ABC

from classes.classes import Vacancy
from settings import VACANCIES


class HhAPIData(ABC):
    """Абстрактный класс для работы с API"""

    def get_vacancies(self, keyword, count_page) -> list[Vacancy]:
        pass


class JSONSaver(ABC):
    """Абстрактный класс для записи в JSON и чтения данных"""

    def read_data(self, path: str = VACANCIES):
        """Чтение данные в JSON файл"""
        pass

    def writing_data(self, data: list, path: str = VACANCIES):
        """Запись данные в JSON файл"""
        pass

    def save_to_file(self, file_path):
        """Сохраняет информацию о вакансии в файл."""
        pass