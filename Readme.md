# 🎲 Number Guessing Game

Welcome to the **Number Guessing Game**! This interactive game challenges you to guess a randomly generated number within a set number of attempts. Each difficulty level changes the number of attempts, so choose wisely!

**Project Link:** [Number Guessing](https://roadmap.sh/projects/number-guessing-game)

## 📜 Table of Contents
- [Features](#-features)
- [Game Rules](#-game-rules)
- [Difficulty Levels](#-difficulty-levels)
- [Leaderboard](#-leaderboard)
- [Installation](#-installation)
- [Usage](#-usage)
- [Code Overview](#-code-overview)
- [Contributing](#-contributing)

---

## ✨ Features
- **Dynamic Difficulty Selection**: Choose from Easy, Medium, or Hard.
- **Timed Gameplay**: Track your total time to guess the correct number.
- **Leaderboard**: Your performance is saved based on difficulty level.
- **Easy to Reset**: Quickly clear and reset the leaderboard.

## 🎯 Game Rules
1. The game will generate a random number between **1 and 100**.
2. You will have a limited number of attempts to guess the correct number.
3. After each incorrect guess, you'll receive a hint:
   - If the guess is too high, you’ll see “The number is less than [your guess].”
   - If the guess is too low, you’ll see “The number is greater than [your guess].”
4. If you guess the number correctly, your attempts and time are saved to the leaderboard!

## 🕹 Difficulty Levels
| Difficulty | Attempts | Description                                          |
|------------|----------|------------------------------------------------------|
| Easy       | 10       | Plenty of attempts to help you get familiar with the game. |
| Medium     | 5        | A balanced challenge for those ready for more focus. |
| Hard       | 3        | Limited attempts to test your guessing skills!       |

## 🏆 Leaderboard
Each successful game records the number of attempts you used to guess the number. You can view, reset, or continue to update your leaderboard based on performance across each difficulty level.

### Displayed as:
+--------------+----------+
| Difficulty   |   Values |
+==============+==========+
| Easy         |        9 |
+--------------+----------+
| Medium       |        5 |
+--------------+----------+
| Hard         |        3 |
+--------------+----------+

## 💻 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game

2. Ensure tabulate is installed:
   ```bash
   pip install tabulate

3. Run the Game:
   ```bash
   python main.py

## 🚀 Usage
1. **Start the Game**: Run the game by executing the Python script.
   ```bash
   python main.py

2. **Select the option**:  You’ll be presented with three options:
   `1. Start the Game:` Begin a new game.
   `2. Show LeaderBoard:` View and manage the leaderboard.
   `3. Exit the Game:` Exit the program.

3. **Playing the Game:**
   - Choose your difficulty level (Easy, Medium, or Hard).
   - Enter your guesses based on hints provided after each attempt:
   - If your guess is too high, you’ll see a message: “The number is less than [your guess].”
   - If your guess is too low, you’ll see: “The number is greater than [your guess].”
   - Continue until you either guess the number correctly or run out of attempts.
   - When you guess correctly, your number of attempts and the time taken will be recorded on the leaderboard.   

4. **Viewing and Managing the Leaderboard:**
    - The leaderboard shows your best scores for each difficulty level.
    - You can reset the leaderboard by selecting the reset option.
    - View the leaderboard as a tabulated display, for easy comparison of your attempts across difficulty levels.

5. **Exiting the Game:**  Choose the option to exit when you’re done playing.

## 🧩 Code Overview
The code is organized into functions that handle different parts of the game. Here’s a breakdown of the main functions:

- **difficulty(number, turns, max_turns, diffic)**: Manages the main gameplay loop for each difficulty level. This function processes player guesses, gives hints, and updates the leaderboard if the player wins.
- **winning(result, starttime, endtime)**: Determines if the player has won or lost based on their attempts. It also calculates the time taken to guess the correct number and updates the leaderboard stored in the JSON file.
- **startgame()**: Initiates the game session, allows the player to select a difficulty level, and starts the gameplay with the chosen difficulty.
- **display(leaderboard)**: Displays the leaderboard in a formatted table and provides options to reset or return to the game menu.
- **Main Program (if __name__ == "__main__")**: The game’s main loop, which presents options to start a new game, view the leaderboard, or exit.


