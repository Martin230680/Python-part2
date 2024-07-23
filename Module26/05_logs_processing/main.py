import os

def error_log_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

input_file_path = os.path.join('data', 'work_logs.txt')
output_file_path = os.path.join('data', 'output.txt')

logpath_file = os.path.abspath(input_file_path)
outpath_file = os.path.abspath(output_file_path)

print(logpath_file)
print(outpath_file)

try:
    with open(outpath_file, 'w', encoding='utf-8') as output:
        for error_line in error_log_generator(logpath_file):
            output.write(error_line)
    print("Файл успешно обработан.")
except IOError as e:
    print(f"Произошла ошибка при работе с файлами: {e}")

