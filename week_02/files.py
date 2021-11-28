'''
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
'''

def main():
    with open('referat.txt','r', encoding='utf-8') as f:
        content = f.read()
    print(content)
    print("длина =", len(content))
    count = 0
    for word in content.split(' '):
        count += 1
    print("Количество слов:", count)

    content = content.replace(".","!")
    print(content)
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    main()