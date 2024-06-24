from src.classes.Vacancy import Vacancy


def sorted_vacancies_by_date(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортирует список вакансий по дате публикации.
    :param vacancies: Список экземпляров класса Vacancy.
    :return: Отсортированный список экземпляров класса Vacancy.
    """
    return sorted(vacancies)


def sorted_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортирует список вакансий по зарплате (от меньшей к большей).
    :param vacancies: Список экземпляров класса Vacancy.
    :return: Отсортированный список экземпляров класса Vacancy.
    """
    return sorted(vacancies, key=lambda x: (x.get_salary_from or float('inf')))

