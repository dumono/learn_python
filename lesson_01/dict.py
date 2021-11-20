mydic={"city":"Москва", "temperature":"20"}
print(mydic.get('city'))
mydic["temperature"] = int(mydic.get("temperature")) - 5
print(mydic)
mydic.get('country')
print(mydic.get('country', 'Россия'))
mydic["date"] = "27.05.2019"
print(len(mydic))
