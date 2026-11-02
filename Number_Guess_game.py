import random

number = random.randint(1, 50)

for i in range(7):
    guess = int(input("Guess a number (1-50): "))

    if guess == number:
        print("You win!")
        break

    elif guess < number:
        print("Too low!")

    else:
        print("Too high!")

else:
    print("Game over! The number was", number)