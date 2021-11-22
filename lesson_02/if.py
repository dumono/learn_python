def check_weather(temperature):
    if temperature < 0:
        return 'на улице холодно'
    elif temperature < 15:
        # такого условия достаточно, т.к. при выполнении 1 условия мы выходим из функции
        return 'на улице прохладно'
    elif temperature < 25:
        return 'на улице тепло'
    # здесь else не обязательно, т.к. мы осуществляем выход из функции во всех других случаях
    return 'на улице жарко'

print(check_weather(-1))
print(check_weather(8))
print(check_weather(21))
print(check_weather(32))
