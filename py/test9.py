
h = input("1, 2, help: ")

if h == "help":
    print("1 - Unix systems")
    print("2 - Windows systems")
    h = input("1, 2, help: ")
    if h == "1":
        print("Вы выбрали Unix")
    elif h == "2":
        print("Вы выбрали Windows")
elif h == "1":
    print("Вы выбрали Unix")
elif h == "2":
    print("Вы выбрали Windows")
else:
    print("Выбирите что-то другое")

    h = input("1, 2, help: ")

    if h == "help":
        print("1 - Unix systems")
        print("2 - Windows systems")
    elif h == "1":
        print("Вы выбрали Unix")
    elif h == "2":
        print("Вы выбрали Windows")
    else:
        print("Выбирите что-то другое")

