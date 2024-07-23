class File:
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name

    def __enter__(self):
        try:
            self.file = open(self.file_name, 'r', encoding='utf-8')
        except FileNotFoundError:
            print(f"Файл '{self.file_name}' не существует. Создаем новый файл.")
            self.file = open(self.file_name, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        if issubclass(exc_type, IOError):
            print(f"Произошло исключение: {exc_type}, {exc_val}")
            return True


with File('example.txt') as file:
    file.write('Пример текста\n')

