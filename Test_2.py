
# Задание 2. Написать программу на python, которая принимает на вход число в виде 100.00
# И выводит это же число в виде 100 рублей 00 копеек

from decimal import Decimal

rubles_words = {1: "рубль", 2: "рубля", 3: "рублей"}
kopeck_words = {1: "копейка", 2: "копейки", 3: "копеек"}

def get_rubles_in_words(num):
    """Function takes in an integer and returns the correct 
    form of the word rubles to be used with it"""
    pre_last_digit = int(num % 100 / 10)

    if pre_last_digit == 1:
        return rubles_words[3]

    elif num % 10 == 1:
        return rubles_words[1]

    elif num % 10 in [2, 3, 4]:
        return rubles_words[2]

    else:
        return rubles_words[3]

def get_kopecks_in_words(num):
    """Function takes in an integer and returns the correct 
    form of the word kopeck to be used with it"""
    pre_last_digit = int(num % 100 / 10)

    if pre_last_digit == 1:
        return kopeck_words[3]

    elif num % 10 == 1:
        return kopeck_words[1]

    elif num % 10 in [2, 3, 4]:
        return kopeck_words[2]

    else:
        return kopeck_words[3]



num = input("Введите положительное десятичное число в формате 100.00: ")

try: 
    num = Decimal(num)
except:
    print("Неправильный формат ввода. Введите положительное десятичное число в формате 100.00: ")
    quit()

while num < 0:
    num = Decimal(input("Число должно быть больше 0: "))

num = round(num, 2)
lst_num = str(num).split('.')
rubles_in_num = int(lst_num[0])
kopecks_in_num = int(lst_num[1])

rubles_in_words = get_rubles_in_words(rubles_in_num)
kopecks_in_words = get_kopecks_in_words(kopecks_in_num)

print(f"Ваша сумма: {rubles_in_num} {rubles_in_words} {kopecks_in_num} {kopecks_in_words}.")




