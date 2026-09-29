import random

secret=random.randint(1,100)

print("Number guesssing game")



while True:
    try:
        guess = int(input("Enter your guess:"))
        if guess > secret:
            print("Too high")
            
        elif guess < secret:
             print("too low")

        elif guess == secret:
            print("Correct")
            break
    except:
        print("please enter an valid guess between 1 to 100")
