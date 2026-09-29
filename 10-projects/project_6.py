while True:
    print("==== student login ====")
    print(1,"Create an account")
    print(2,"Login")
    print(3,"Exit")

    choice = input("Enter your choice :")

    if choice == "1":
        username = input("Create your username:")
        password = input("create  your password:")
        studentname = input("Enter your name:")
        print("successfully account created")

    elif choice == "2":
        username1 = input("Enter your username:")
        password2 = input("Enter your password:")
        if username1 == "Akash" and password1 == "12345":
            print("Successfully logged in")
            print("Welcome Akash")
            print("Show my name")
            print("Change my password")
            print("Logout")
            nextwhat = input("Enter your next choice :")
            if nextwhat == "logout":
                break
            elif nextwhat == "continue":
                print("Alright")
           

    elif choice == "3":
        break




    





    

