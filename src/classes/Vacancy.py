from datetime import datetime


class Vacancy:
    """Класс для представления вакансии."""

    def __init__(self, name, area, salary_from, salary_to, currency,
                 experience, published_at, alternate_url):
        self.__name: str = name  # Название вакансии.
        self.__area: str = area  # Город, в котором расположена вакансия.
        self.__salary_from: int or None = salary_from  # Минимальная зарплата.
        self.__salary_to: int or None = salary_to  # Максимальная зарплата.
        self.__currency: str or None = currency  # Валюта зарплаты.
        self.__experience: str or None = experience  # Требуемый опыт работы.
        self.__published_at: str = published_at  # Дата публикации вакансии в формате ISO 8601.
        self.__alternate_url: str = alternate_url  # Ссылка на вакансию.

    @property
    def get_name(self) -> str:
        return self.__name

    @property
    def get_area(self) -> str:
        return self.__area

    @property
    def get_salary_from(self) -> int or None:
        return self.__salary_from

    @property
    def get_salary_to(self) -> int or None:
        return self.__salary_to

    @property
    def get_currency(self) -> str or None:
        return self.__currency

    @property
    def get_experience(self) -> str or None:
        return self.__experience

    @property
    def get_published_at(self) -> str:
        return self.__published_at

    @property
    def get_alternate_url(self) -> str:
        return self.__alternate_url

    def to_dict(self) -> dict:
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

    def __lt__(self, other) -> bool:
        """Определяет оператор '<' для сравнения по дате публикации."""
        return self.__published_at < other.__published_at

    def __gt__(self, other) -> bool:
        """Определяет оператор '>' для сравнения по дате публикации."""
        return self.__published_at > other.__published_at

    def lt__salary(self, other) -> bool:
        """Определяет оператор '<' для сравнения по зарплате."""
        if self.__salary_from is None:
            return False
        if other.__salary_from is None:
            return True
        return self.__salary_from < other.__salary_from

    def gt__salary(self, other) -> bool:
        """Определяет оператор '>' для сравнения по зарплате."""
        if self.__salary_from is None:
            return True
        if other.__salary_from is None:
            return False
        return self.__salary_from > other.__salary_from

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Vacancy."""
        return (f"Название вакансии: {self.__name}\n"
                f"Город: {self.__area}\n"
                f"{self.validate_salary()}\n"
                f"Дата публикации: {self.formatting_date()}\n"
                f"Ссылка на вакансию: {self.__alternate_url}\n"
                f"Опыт работы: {self.__experience}\n")
