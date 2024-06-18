from abc import ABC, abstractmethod

from settings import VACANCIES_JSON


class BaseAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword: str, count_page: int) -> list[object]:
        pass


class JSONSaver(ABC):
    """Абстрактный класс для записи в JSON и чтения данных"""

    @abstractmethod
    def read_data(self, path: str = VACANCIES_JSON):
        """Чтение данные в JSON файл"""
        pass

    @staticmethod
    def writing_data(data: list, path: str = VACANCIES_JSON):
        """Запись данные в JSON файл"""
        pass

