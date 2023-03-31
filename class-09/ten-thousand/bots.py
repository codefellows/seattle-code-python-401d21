"""Place in root of Project,
at same level as pyproject.toml
"""

from abc import ABC, abstractmethod
import builtins
import re
from ten_thousand.game import play
from ten_thousand.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game bots"""

    def __init__(self, print_all=False):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))
            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))
        elif line.startswith("*** "):
            self.last_roll = [int(ch) for ch in line if ch.isdigit()]
        else:
            self.last_print = line
        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""
        if self.last_print == "(y)es to play or (n)o to decline":
            return "y"
        elif self.last_print == "Enter dice to keep, or (q)uit:":
            return self._enter_dice()
        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":
            return self._roll_bank_or_quit()
        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        for value in roll:
            roll_string += str(value)
        self.report("> " + roll_string)
        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""
        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""
        mega_total = 0
        for _ in range(num_games):
            player = cls()
            try:
                play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass
            mega_total += player.total_score
            player.reset()
        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class MiddlingMargaret(BaseBot):
    """MiddlingMargaret has a moderate playing style"""

    def _roll_bank_or_quit(self):

        if self.unbanked_points >= 500 or self.dice_remaining < 3:
            return "b"

        return "r"


class DaringDarla(BaseBot):
    """DaringDarla rolls whenever more than 1 dice remaining """

    def _roll_bank_or_quit(self):
        if self.dice_remaining == 1:
            return "b"

        return "r"


class YoniBot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 550 or self.dice_remaining < 2:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining <= 3:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 2:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"


class EvilBrendan(BaseBot):
    """VERY aggressive playstyle : all or nothing baby"""

    def _roll_bank_or_quit(self):
        if self.dice_remaining >= 3:
            return "r"
        if self.unbanked_points >= 800 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points > 350:
            if self.dice_remaining >= 3:
                return "r"
            else:
                return "b"
        if self.unbanked_points <= 400:
            return "r"

class TheBestBot(BaseBot): #sheldon and mike

    start_dict = {
        1: 200,
        2: 150,
        3: 400,
        4: 750,
        5: 2300,
        6: 4850
    }

    def _roll_bank_or_quit(self):
        if self.unbanked_points <= TheBestBot.start_dict[self.dice_remaining]:
            return 'r'
        return 'b'

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        return super()._enter_dice()


class Not_too_shabby(BaseBot):
    def _roll_bank_or_quit(self):
        """Our playstyle is heavily based on EvilBrendan with some conditional alterations"""
        if self.dice_remaining >= 4:
            return 'r'
        if self.unbanked_points >= 600 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points > 200:
            if self.dice_remaining >= 4:
                return 'r'
            else:
                return 'b'
        if self.unbanked_points < 200:
            return 'r'

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        return super()._enter_dice()


class JamesAndTreBot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 500:
            return 'b'
        elif self.unbanked_points >= 350:
            return 'r'
        elif self.dice_remaining == 0:
            return 'b'
        elif GameLogic.get_scorers(self.last_roll):
            return 'r'
        else:
            return 'q'


class RollingThunder(BaseBot): # Ethan Domique
    def _roll_bank_or_quit(self):
        if self.dice_remaining > 3 or self.unbanked_points < 300:
            return 'r'
        return "b"




class YourBot(BaseBot):

    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 800 or self.dice_remaining < 2:
            return "b"
        if self.unbanked_points >= 300 and self.dice_remaining <= 3:
            return "b"
        elif self.unbanked_points >= 200 and self.dice_remaining == 2:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"


















if __name__ == "__main__":
    num_games = 10000
    # NervousNellie.play(num_games)
    # MiddlingMargaret.play(num_games)
    # DaringDarla.play(num_games)
    # TheBestBot.play(num_games) # 10617
    # Not_too_shabby.play(num_games) # 10453
    # JamesAndTreBot.play(num_games) #8622
    # RollingThunder.play(num_games) #10538
    # YourBot.play(num_games) # 9937

