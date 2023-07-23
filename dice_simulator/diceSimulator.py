import random

print("""
Enter a number to start.
Enter 'exit' if you don't wanna play it
""")


def roll_dice(amount: int = 2):
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):

        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)
    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice would you like roll> ")
            if user_input.lower() == "exit":
                print("Good bye!")
                break

            print(*roll_dice(int(user_input)), sep=", ")
        except ValueError:
            print("Number must require!")


if __name__ == "__main__":
    main()
