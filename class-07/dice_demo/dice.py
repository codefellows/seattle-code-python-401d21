from random import randint

def default_roller(dice=6):
    for di in range(dice):
        return_dice = randint(1, 6)

def play_dice(roller=default_roller()):
    print("Enter r to roll or q to quit")
    choice = input("> ")
    if choice.lower() == "q":
        print("OK, Bye!")
    else:
        roll = roller
        print(roll)


if __name__ == '__main__':
    # print(default_roller())
    play_dice()
