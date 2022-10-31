import random

num = random.randint(1, 100)
life = 6

while life > 0:
    guess = int(input("guess number: "))
    life -= 1
    if guess > num:
        print(f"Lower than {guess} life {life}")
    elif guess < num:
        print(f"Higher than {guess} life {life}")
    else:
        print("Game clear")
        break

if life == 0:
    print("Game Over")