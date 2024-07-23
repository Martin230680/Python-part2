from typing import Tuple


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string: str) -> list:
        try:
            day, month, year = date_string.split('-')
            day = int(day)
            month = int(month)
            year = int(year)
            if cls.is_valid_date(day, month, year):
                data_list = [day, month, year]
                return data_list
            else:
                raise ValueError
        except ValueError:
            raise ValueError("Некорректный формат даты. Формат даты должен быть - 'dd-mm-yyyy' dd - [1-31], "
                             "в зависимости от месяца и года  mm -[1-12], я год не меньше 1")

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int) -> bool:
        if year < 1:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return day <= 31
        elif month in {4, 6, 9, 11}:
            return day <= 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return day <= 29
            else:
                return day <= 28
        else:
            return False

    def __str__(self) -> str:
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

# Пример использования:
try:
    date_str = input("Введите дату в формате 'dd-mm-yyyy': ")
    date = Date.from_string(date_str)
    print(f"Дата: {date[0]}-{date[1]}-{date[2]}")
except ValueError as e:
    print("Ошибка:", e)