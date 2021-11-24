def main():
    rating_list = [7,4,2]
    while True:
        try:
            new_element = int(input("Введите новый элемент рейтинга (натуральное число): "))
        except ValueError:
            print("Вы ввели не {целое/натуральное} число")
            continue

        if new_element < 1:
            print ("Вы ввели ненатуральное число")
            continue
        new_rating_list = []
        for index, rate in enumerate(rating_list):
            if new_element > rate:
                if index == 0:
                    new_rating_list.append(new_element)
                else:
                    new_rating_list = rating_list[:index]
                    new_rating_list.append(new_element)
                new_rating_list += rating_list[index:]
                rating_list = new_rating_list
                break
            if index == (len(rating_list) - 1):
                rating_list.append(new_element)
                break
        print(rating_list)


if __name__ == "__main__":
    main()