def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def add_and_multiply_fractions(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split("/"))
    num2, denom2 = map(int, fraction2.split("/"))

    # Находим общий знаменатель
    common_denom = denom1 * denom2 // gcd(denom1, denom2)

    # Приводим дроби к общему знаменателю
    new_num1 = num1 * (common_denom // denom1)
    new_num2 = num2 * (common_denom // denom2)

    # Сумма дробей
    sum_num = new_num1 + new_num2

    # Произведение дробей
    product_num = num1 * num2
    product_denom = denom1 * denom2

    return f"{sum_num}/{common_denom}", f"{product_num}/{product_denom}"


fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

sum_result, product_result = add_and_multiply_fractions(fraction1, fraction2)
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)
