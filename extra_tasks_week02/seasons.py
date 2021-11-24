
def getSeasonList(num_month):
    listMonthsSeason = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень',
                        'осень', 'осень', 'зима']
    return listMonthsSeason[num_month - 1]

def getSeasonDict(num_month):
    dictMonthsSeason = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
                        7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
    return dictMonthsSeason[num_month]

def main():
    try:
        month = int(input("Введите номер месяца (1-12):"))
    except ValueError:
        print("Вы ввели не число")
        exit(-1)
    if 1 <= month <= 12:
        print('Это {}'.format(getSeasonList(month)))
        print("------------------")
        print('Это {}'.format(getSeasonDict(month)))
    else:
        print("Введенное число не является номером месяца")

if __name__ == "__main__":
    main()