def main():
    userString = str(input("Введите длинную строку: "))
    for index, word in enumerate(userString.split(' ')):
        print(index, word[:10])

if __name__ == '__main__':
    main()