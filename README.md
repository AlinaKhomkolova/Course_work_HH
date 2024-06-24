## Курсовой проект по курсу «API и библиотека requests»

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?style=flat-square&logo=Pytest)](https://docs.pytest.org/en/8.2.x/)
[![Requests](https://img.shields.io/badge/-Requests-464646?style=flat-square&logo=Requests)](https://pypi.org/project/requests/)

### Технологии:

- Python 3.10.12
- pytest-cov 5.0.0
- requests 2.32.3

### Задание

Напишите программу, которая будет получать информацию о
вакансиях с платформы hh.ru в России, сохранять ее в файл и
позволять удобно работать с ней: добавлять, фильтровать, удалять.

### Критерии выполнения курсовой работы:

- Проект выложили на GitHub.
- Из файла README понятно, о чём проект и как его использовать.
- В Git есть точечные коммиты.
- Код программы грамотно разбит на функции/классы/модули/пакеты.
- Код читабельный (хороший нейминг, есть docstring, используется typing).
- В работе используются абстрактные классы (минимум один).
- В работе есть переопределение магических методов.
- Для работы с API используется библиотека requests.
- В ходе работы программы создается файл со списком вакансий.
- Пользователь может вывести из файла набор вакансий по определенным критериям.
- Код покрыли тестами (опционально).

### Инструкция для развертывания проекта:

#### Клонирование проекта:

```bash
git clone git@github.com:AlinaKhomkolova/Course_work_HH.git
```

```bash
cd Course_work_HH
```

#### Создать виртуальное окружение:

```bash
python -m venv venv
```

#### Активировать виртуальное окружение:

Для Linux

```bash
source venv/bin/activate
```

Для Windows

```bash
venv\Scripts\activate.bat
```

#### Установить зависимости:

```bash
pip install -r requirements.txt
```

#### Открыть проект в PyCharm.

Автор проекта Хомколова Алина