# LAB - Class 08
## Project: ten-thousand - version 3
## About this lab:
As we were unable to complete all feature tasks from yesterday's lab, this is the solution code and bot file forked and pulled from the class repo per Roger. We did not write any of the game logic, game code, game state, tests, ect. The only file we modified is the bots.py to build our gameplay bot.
## Feature Tasks and Requirements:
- Create an AI Bot to play Ten Thousand
The only method available for use from Game class is play.
All static methods of GameLogic class are available.
All other interactions with game can take place ONLY via the I/O features of the game.
In other words, via injectable print and input functionality.
It is FORBIDDEN to inject a custom roller function into Game class.

Author: Tyler Huntley & Dutch Foy (We only modified `bots.py` file `class YourBot`.)
Links and Resources
[ChatGPT](https://openai.com/)
[Class Repo](https://github.com/codefellows/seattle-code-python-401d21)
How to initialize/run your application (where applicable)
python ten-thousand/game_logic.py
python bots.py
How to use your library (where applicable)
Tests
How do you run tests?
pytest -k version_#



# Ten Thousand Game

## Version 1

- GameLogic class
  - roll_dice
  - calculate_score

- Banker
  - deposit/bank
  - shelf
  - clear

## Version 2

- beginning Game class
  - allows banking or quitting on first roll of multiple rounds
  - no rerolls
  - no zilches
  - no cheating checks
- Introducing Flow testing with Flo

## Version 3

- validate_keepers
- get_scorers
- Advanced Game class
  - rerolls allowed
  - using all six dice resets to six dice
  - zilches happen
  - cheating is checked

## Version 4

- Bot time
