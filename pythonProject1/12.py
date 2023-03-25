width = float(input('Введите ширину'))
height = float(input('Введите длину'))
expenditure = int(input('Введите расход'))
volume = int(input('Объем банки в литрах'))
percent = int(input('Введите процент запаса'))
s = round((width * height), 2)
print(s)
liters = (width * height / expenditure)
liters *= 0.2 + liters
print(liters)
cans = round(s / expenditure / volume)+1
print(cans)


# percent = percent*0.2 + percent/