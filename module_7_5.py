import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = f'{root}\\{os.path.join(file)}'
        filetime = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file}'
              f', Путь: {file_path}'
              f', Размер: {file_size} '
              f'байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')

