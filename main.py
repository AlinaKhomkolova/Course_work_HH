import requests

from classes.HhAPI import HhAPI
from classes.Saver import WritingReadingData
from classes.UserInterface import UserInterface
from src.utils import sorted_vacancies_by_date, sorted_vacancies_by_salary


def main():
    user_interface = UserInterface()

    # Получаем данные от пользователя
    search_by_request, count_page = user_interface.get_user_input()
    if search_by_request is None or count_page is None:
        return

    try:
        # Инициализируем API HeadHunter
        hh_api = HhAPI()

        # Получаем список вакансий
        vacancies = hh_api.get_vacancies(search_by_request, count_page)
    except requests.RequestException as e:
        user_interface.display_error(f"Ошибка запроса: {e}")
        return
    except Exception as e:
        user_interface.display_error(f"Произошла ошибка: {e}")
        return

    # Получаем выбор пользователя по сортировке
    sort_option = user_interface.get_sort_option()
    if sort_option == 1:
        # Сортировка по дате публикации
        sorted_vacancies_list = sorted_vacancies_by_date(vacancies)
    elif sort_option == 2:
        # Сортировка по зарплате
        sorted_vacancies_list = sorted_vacancies_by_salary(vacancies)
    else:
        user_interface.display_error("Некорректный выбор опции.")
        return

    # Отображаем отсортированные вакансии
    user_interface.display_vacancies(sorted_vacancies_list)

    # Просим пользователя сохранить данные, если он согласен
    if user_interface.ask_to_save():
        try:
            # Сохраняем данные в текстовый файл
            WritingReadingData.writing_data_txt(sorted_vacancies_list)
        except Exception as e:
            user_interface.display_error(f"Ошибка при сохранении данных: {e}")


if __name__ == '__main__':
    main()
