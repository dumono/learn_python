def is_real_positive_number(number):
    try:
        number = float(number)
    except ValueError:
        return False
    if number > 0:
        return True
    return False

def is_int_negative_number(number):
    try:
        number = int(number)
    except ValueError:
        return False
    if number < 0:
        return True
    return False

def is_even_number(number):
    if number % 2 == 0:
        return True
    return False

def my_func(number,power):
    if power < 0:
        return 1 / my_func(number, abs(power))
    if power == 1:
        return number
    if power == 2:
        return number * number
    if not is_even_number(power):
        a = my_func(number, (power-1)/2)
        return a * number * a
    a = my_func(number, power/2)
    return a * a


def main():
    x = float(input("Введите число, которое будете возводить в степень: "))
    y = int(input("Введите степень числа: "))
    if not is_real_positive_number(x):
        print("Параметр {0} не удовлетворяет условиям".format(x))
        exit(-1)
    if not is_int_negative_number(y):
        print("Параметр {0} не удовлетворяет условиям".format(y))
        exit(-1)

    print("Результат:", my_func(x, y))

if __name__ == "__main__":
    main()
