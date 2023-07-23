from random import randint

lower_number, higher_number = 1, 10
random_number: int = randint(lower_number, higher_number)

print(f"Guess the number in range from {lower_number} to {higher_number}!")

while True:
    try:
        user_guess: int = int(input("Guess> "))
    except ValueError as e:
        print("Number must require!")
        continue

    if user_guess > random_number:
        print("Number is Lower!!!")
    elif user_guess < random_number:
        print("Number is Higher!!!")
    else:
        print("Correct!!!")
        break
