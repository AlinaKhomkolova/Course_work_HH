class UserInterface:
    def __init__(self):

        self.search_by_request: str = ''  # Инициализация пустой строки
        self.count_page: int = 0  # Инициализация количества страниц от пользователя
        self.sort_option: int = 0  # Инициализация опций для сортировки от пользователя
        self.add_answer_user: bool = False  # Инициализация логического значения False

    def get_user_input(self):
        """Получает ввод пользователя для поиска вакансий."""
        try:
            self.search_by_request = input("Введите название профессии, должность или компанию:\n").strip()
            if self.search_by_request == '':
                self.display_error('Поисковой запрос не задан.')
                return None, None

            self.count_page = int(input("Сколько страниц вы хотите просмотреть?\n"
                                        "(На одной странице располагается 10 вакансий)\n"))
            return self.search_by_request, self.count_page
        except ValueError:
            self.display_error("Некорректный ввод. Введите числовое значение для параметра, 'Количество страниц'.")
            return None, None

    def get_sort_option(self) -> int:
        """Получает выбор пользователя для сортировки вакансий."""
        print("Отсортировать вакансии по:\n"
              "1. Дате публикации\n"
              "2. Зарплате\n")
        self.sort_option = int(input("Выберите опцию (1/2)\n"))
        return self.sort_option

    def ask_to_save(self) -> bool:
        """Спрашивает пользователя о сохранении отсортированных вакансий."""
        print("Добавить отсортированные вакансии в избранное(vacancies_hh.txt)?")
        self.add_answer_user = input("Да/Нет\n").lower()
        return self.add_answer_user == "да"

    @staticmethod
    def display_vacancies(sorted_vacancies_list: list):
        """Выводит список отсортированных вакансий."""
        for vacancy in sorted_vacancies_list:
            print(vacancy)

    @staticmethod
    def display_error(message: str):
        """Выводит сообщение об ошибке"""
        print(f"Ошибка: {message}")
