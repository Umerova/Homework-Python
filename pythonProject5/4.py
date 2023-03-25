lst = []  # создаем пустой список

while True:
    surname = input("Введите фамилию преподавателя (или 'стоп' для завершения ввода): ")
    if surname.lower() == "стоп":
        break

    position = input("Введите должность: ")

    while True:
        try:
            students = int(input("Введите количество студентов во всех группах: "))
            break
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте еще раз.")

    # создаем список с информацией и добавляем его в общий список
    info = [surname, position, students]
    lst.append(info)

print("Информация о преподавателях:")
for i in range(len(lst)):
    print(f"{i + 1}. Фамилия: {lst[i][0]}, Должность: {lst[i][1]}, Количество студентов во всех группах: {lst[i][2]}")

