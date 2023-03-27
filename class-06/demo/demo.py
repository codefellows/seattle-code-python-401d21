import random
# create a class for GameLogic
# rolls 2 dice
# total the roll from 2 dice


class GameLogic:

    # @staticmethod
    # the dice parameter will be a tuple of the number of dice
    def dice_roller(self, dice):
        # Generates a random number between 1-6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return_dice = tuple((dice1, dice2))
        return return_dice


if __name__ == '__main__':
    new_game = GameLogic()
    print(new_game)
    print(new_game.dice_roller(2))
