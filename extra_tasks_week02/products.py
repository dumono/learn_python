def askYesNo(question):
    while True:
        ask = str(input(question)).lower()
        if ask == 'y' or ask == 'д':
            return True
        if ask == 'n' or ask == 'н':
            return False
        print("Ответ неверный. Введите Y/N")

def getAnalyse(products):
    products_properties = []
    # получаем список всех свойств для всех товаров внутри объекта
    for prod in products:
        product_prop = prod[1].keys()
        for prop in product_prop:
            products_properties.append(prop)
    #выделяем только уникальные свойства
    uniq_properties = sorted(list(set(products_properties)))
    analyseDict = {}
    for prod in products:
        for analyse_prop in uniq_properties:
            key = prod[1].get(analyse_prop) #получаем текущее значение свойства
            # пытаемся получить старые значения, если None, то добавляем текущее значение
            old_key = [analyseDict.get(analyse_prop)]
            if old_key == [None]:
                analyseDict[analyse_prop] = key
            else:
                # если уже есть значения, то к ним добавляем новое
                old_key.append(key)
                analyseDict[analyse_prop] = old_key

    #получение только уникальных значений для свойств вынесен из основного цикла
    for analyse_prop in uniq_properties:
        analyseDict[analyse_prop] = sorted(list(set(analyseDict.get(analyse_prop))))
    return analyseDict

def main():
    products = []
    while True:

        product_id = len(products) + 1
        # будем считать что пока у нас пользователь понимает, что вводит
        new_product_dict = {'Название': str(input("Введите название товара: ")),
                            'Цена': int(input("Введите цену товара: ")),
                            'Количество': int(input("Введите количество товара: ")),
                            'Единицы': str(input("Введите единицы товара: "))}

        product = (product_id, new_product_dict)
        products.append(product)
        if askYesNo("Продолжить ввод? "):
            continue
        print(products)
        print(getAnalyse(products))
        break


if __name__ == "__main__":
    main()