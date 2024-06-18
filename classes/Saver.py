import json

from settings import VACANCIES_TXT, VACANCIES_JSON
from classes.ABC_classes import JSONSaver


class WritingReadingData(JSONSaver):

    def read_data(self, path: str = VACANCIES_JSON) -> list[dict]:
        """
        Читает данные из файла.
        Args:
            path (str): Путь к файлу с данными.
        Returns:
            list: Список данных из файла.
            """
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def writing_data_JSON(data: list, path: str = VACANCIES_JSON) -> None:
        with open(path, "r", encoding="utf-8") as file:
            try:
                existing_data = json.load(file)
            # Если файл пустой или поврежден, начинаем с пустого списка
            except json.JSONDecodeError:
                existing_data = []

        # Преобразуем каждый объект Vacancy в словарь и добавляем к существующим данным
        json_data = [vacancy.to_dict() for vacancy in data]
        existing_data.extend(json_data)

        # Записываем обновленные данные в JSON файл с отступами для читаемости
        with open(path, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def writing_data_txt(data: list, path: str = VACANCIES_TXT) -> None:
        with open(path, "a", encoding="utf-8") as file:
            for vacancy in data:
                file.write(str(vacancy))
                file.write("\n")
