import os
from typing import Iterator, Tuple

def line_counter(mypath_directory: str) -> Iterator[Tuple[int, str]]:
    print(f'Текущая директория: {mypath_directory}')
    for root, dirs, files in os.walk(mypath_directory):
        for i_file in files:
            if i_file.endswith('.py'):
                file_path = os.path.join(root, i_file)
                print('***********************************************************')
                print('Открываю', file_path)
                print('***********************************************************')
                count: int = 0
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if line.strip() and not line.strip().startswith('#'):
                            count += 1
                            yield count, line.strip()
                    print(f'В файле всего:{count} строк удовлетворяющие условию\n')

mypath_directory: str = os.path.abspath(os.path.join('..', ))
for count, line in line_counter(mypath_directory):
    print(f'\t{count}\t{line}')