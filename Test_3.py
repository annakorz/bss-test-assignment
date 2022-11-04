# Задание 3. Написать программу на python, содержащую функцию, принимающую на вход файл JSON 
# и выводящую на экран содержимое структуры данных в виде ключ - значение.
# В случае наличия в JSON вложенных структур, выводить их с отступом в символ табуляции.

import json

def get_json_content(file_name):
    """Function takes in a JSON-file and prints out its content"""
    with open(file_name, 'r') as file:
        data = json.load(file)
    content = json.dumps(data, sort_keys=True, separators=(',', ' - '), indent='\t')

    return print(content)

file_name = 'weather_data.json'

get_json_content(file_name)











    