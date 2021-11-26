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

def number_power(number, power):
    if power == 1:
        return number
    if not is_even_number(power):
        return number_power(number, power/2) * number * number_power(number, power/2)
    else:
        return number_power(number, power/2) * number_power(number, power/2)

def my_func(x,y):

    return 1 / number_power(x, abs(y))

def main():
    x = float(input ("Введите число, которое будете возводить в степень: "))
    y = int(input ("Введите степень числа: "))
    if not is_real_positive_number(x):
        print ("Параметр {0} не удовлетворяет условиям".format(x))
        exit(-1)
    if not is_int_negative_number(y):
        print ("Параметр {0} не удовлетворяет условиям".format(y))
        exit(-1)

    print ("Результат:", my_func(x,y))

if __name__ == "__main__":
    main()
