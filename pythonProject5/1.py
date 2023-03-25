playgame = input("Введите настольную игру или 0, чтобы закончить")
games = []
while playgame != "0":
    if playgame in games:
        print("эта игра уже записана")
        playgame = input("Введите настольную игру или 0, чтобы закончить")
    else:
        games.append(playgame)
    playgame = input("Введите настольную игру или 0, чтобы закончить")
games.sort
print(games)