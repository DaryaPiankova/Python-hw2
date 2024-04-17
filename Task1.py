# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

number_to_hex = int(input("Введите число: "))
check_number_to_hex = number_to_hex
rest = None
result: str = ""
while number_to_hex:
    rest = number_to_hex % 16
    if rest == 10:
        rest = "A"
    elif rest == 11:
        rest = "B"
    elif rest == 12:
        rest = "C"
    elif rest == 13:
        rest = "D"
    elif rest == 14:
        rest = "E"
    elif rest == 15:
        rest = "F"

    result += str(rest)
    number_to_hex //= 16
print(result[::-1])
print("Проверка с помощью hex(): ", (hex(check_number_to_hex)))
