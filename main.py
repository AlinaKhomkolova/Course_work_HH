from classes.classes import HhAPI, Vacancy, WritingReadingData
from settings import VACANCIES_TXT
from src.utils import sorted_vacancies_by_date, sorted_vacancies_by_salary


def main():

    search_by_request = input("Введите название профессии, должность или компанию:\n")
    count_page = int(input("Сколько страниц вы хотите просмотреть?\n"))

    hh_api = HhAPI()
    vacancies = hh_api.get_vacancies(search_by_request, count_page)

    print("Отсортировать вакансии по:\n"
          "1. Дате публикации\n"
          "2. Зарплате\n")
    sort_option = input("Выберите опцию (1/2)\n")
    if sort_option == "1":
        sorted_vacancies_list = sorted_vacancies_by_date(vacancies)
    elif sort_option == "2":
        sorted_vacancies_list = sorted_vacancies_by_salary(vacancies)
    else:
        print("Некорректный выбор опции.")
        return
    print("Добавить отсортированные вакансии в избранное(vacancies_hh.txt)?")
    add_answer_user = input("Да/Нет").lower()
    if add_answer_user == "да":
        writing_data = WritingReadingData()
        writing_data.save_to_file()
    else:
        pass
    for vacancy in sorted_vacancies_list:
        print(vacancy)


if __name__ == '__main__':
    main()
