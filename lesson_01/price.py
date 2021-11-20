def format_price(price):
    convert = int(price)
    return "Цена: " + str(convert) + " руб."

price = format_price(56.24)
print (price)