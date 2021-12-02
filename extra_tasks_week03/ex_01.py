#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

def main():
    try:
        num = int(input("Введите число (1-9999): "))
    except(ValueError):
        print("Ввод не является целым числом")

    if num > 9999:
        print("Число вне диапазона (1-9999)")
        exit(-1)
    else:
        num = abs(num)

    result = 3 * num + 2 * num * (10 ** len(str(num))) + num * (10 ** (2 * len(str(num))))

    print(result)

if __name__ == "__main__":
    main()