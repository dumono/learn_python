def numbers_summ(parameter):
    result = 0
    for number in parameter.split(' '):
        try:
            result += int(number)
        except ValueError:
            if number != '=':
                print("Не получилось прибавить '", number, "'")
            continue
    return result

def main():
    print("Введите строки суммируемых чисел, разделенных пробелами. Для завершения введите '=' в конце.")
    user_summ = 0
    while True:
        summ_string = input("Введите строку:")
        user_summ += numbers_summ(summ_string)
        print(user_summ)
        if summ_string[-1] == "=":
            break




if __name__ == "__main__":
    main()