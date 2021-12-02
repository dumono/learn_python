#Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

def main():
    try:
        num = int(input("Введите положительное число: "))
    except(ValueError):
        print("Ввод не является целым числом")

    if num < 0 :
        print("Число меньше 0")
        exit(-1)

    max = 0
    #первый вариант просто анализом
    #for number in str(num):
    #    if max < number:
    #        max = number
    # второй через while:
    while num > 0:
        number = num % 10
        num = num // 10
        if max < number:
            max = number
    print(max)

if __name__ == "__main__":
    main()