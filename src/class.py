from abc import ABC, abstractmethod


from settings import VACANCIES


class JobAPI(ABC):
    """Абстрактный класс для работы с API сервисами с вакансиями """

    @abstractmethod
    def __init__(self, id_vac, name, area, salary,
                 schedule, snippet, employer, apply_alternate_url,
                 experience, alternate_url):
        pass


class Parser:

    def __init__(self, file_worker):
        self.file_worker = file_worker


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """
    pass

hh_parser = HH(VACANCIES)
hh_parser.load_vacancies('Администратор')
print(hh_parser.vacancies)
