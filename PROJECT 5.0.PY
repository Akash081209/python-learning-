games = ["GTA","Minecraft", "No man's sky"]
while True:
    print("====Game collection====")
    print("1.Add game")
    print("2. remove game")
    print("3. search game")
    print("4. show all numbers of games")
    print("5. show all games")
    print("6 . Exit")

    choice = input("Enter your choice :")

    if choice == "1":
        Addgame = input("Enter the game you want to add:")
        games.append(Addgame)
        print("Game has been added")

    elif choice == "2":
        removegame = input("Enter the game you want to remove:")
        if removegame in games:
            games.remove(removegame)
            print("Game removed")
        else :
            print("not in collection")

    elif choice == "3":
        searchgame = input("Enter game you want search:")
        if searchgame in games:
            print("Its their")
        else:
            print(" not available")

    elif choice == "4":
        print(len(games))

    elif choice == "5":
        print(games)

    elif choice == "6":
        print("bye")
        break  

 