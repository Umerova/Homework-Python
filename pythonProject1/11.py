mass = int(input('Введите массу'))
height = int(input('Введите рост'))
height = height / 100
res = round((mass / height**2), 2)
print(res)