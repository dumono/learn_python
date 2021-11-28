from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_ALL, "russian")
'''
Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
Превратите строку "01/01/25 12:10:03.234567" в объект datetime
'''

def main():

    now = datetime.now()
    print(now.strftime("%d %B %Y"))
    print((now - timedelta(1)).strftime("%d.%m.%Y"))
    print((now - timedelta(30)).strftime("%Y-%m-%d %H:%M"))

    new_date = datetime.strptime("01/01/25 12:10:03.234567", "%d/%m/%y %H:%M:%S.%f")
    print(new_date)

if __name__ == "__main__":
    main()