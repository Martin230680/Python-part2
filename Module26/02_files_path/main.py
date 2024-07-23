import os
from typing import Generator, Optional

def gen_files_path(my_folder: str, mypath_directory: Optional[str] = None) -> Generator[str, None, None]:
    flag: int = 0
    if mypath_directory is None:
        mypath_directory = os.path.abspath(os.path.sep)
    print(f'Директория поиска: {mypath_directory}\n')
    print('Сгенерированные пути файлов при поиске: ')
    for i_root, j_dir, k_file in os.walk(mypath_directory):
        for j in j_dir:
            if j == my_folder:
                flag = 1
            for k in k_file:
                file_path: str = os.path.join(i_root, k)
                yield file_path
                print(file_path)
    if flag == 1:
        print(f'Папка {my_folder} есть')
    else:
        print(f'Папка {my_folder} нет в указанной директории')

mypath_directory: str = os.path.abspath(os.path.join('..', ))
my_folder: str = input('Введите название папки: ')
for i in gen_files_path(my_folder, mypath_directory):
    print(i)