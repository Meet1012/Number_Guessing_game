import random
import time
import json
from tabulate import tabulate

def difficulty(number, turns, max_turns, diffic):
    print(f"\n\nGreat! You have selected the {diffic} difficulty level.")
    print("Let's Start the Game")
    while turns !=  0:
        guess = int(input("\n\nEnter the Guess: "))
        if guess == number:
            leaderboard[diffic] = max_turns - turns
            return max_turns - turns
        elif guess > number:
            print(f"Incorrect! The number is less than {guess}.")
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
        turns -= 1
    return 0

def winning(result, starttime, endtime):
    elapsed_time = endtime - starttime
    formatted = time.strftime("%M:%S", time.gmtime(elapsed_time))
    if result == 0:
            print("\n\nYou are Out of Guesses ! !\n\n")
    else:
        print(f"Congratulations! You guessed the correct number in {result} attempts.")
        print(f"Time Taken to guess: {formatted}\n\n")
        json_file.seek(0)
        json.dump(leaderboard, json_file)
        json_file.truncate()
    return

def startgame():
    print("\n\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")
    number = random.randint(1, 100)
    print("\n\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances) \n\n")
    choices = int(input("Enter the choice: "))
    diff = {1:"Easy", 2:"Medium", 3:"Hard"}
    if choices == 1:
        starttime = time.perf_counter()
        result = difficulty(number, 10, 10, diff[1])
        endtime = time.perf_counter()
        winning(result, starttime, endtime)
        return
        
    elif choices == 2:
        starttime = time.perf_counter()
        result = difficulty(number, 5, 5, diff[2])
        endtime = time.perf_counter()
        winning(result, starttime, endtime)
        return
        
        
    elif choices == 3:
        starttime = time.perf_counter()
        result = difficulty(number, 3, 3, diff[3])
        endtime = time.perf_counter()
        winning(result, starttime, endtime)
        return
    
def display(leaderboard):
    data = [(k,v) for k,v in leaderboard.items()]
    print(tabulate(data,headers=["Difficulty","Values"], tablefmt="grid"))
    print("\n1. Reset LeaderBoards")
    print("2. Back to Game !\n")
    choice = int(input("Enter the Choice: "))
    if choice == 1:
        leaderboard = { "Easy": 10, "Medium": 5, "Hard": 3 }
        json_file.seek(0)
        json.dump(leaderboard, json_file)
        json_file.truncate()
        
    elif choice == 2:
        return 
        
if __name__ == "__main__":
    while True:
        json_file = open("leaderboard.json", "r+")
        leaderboard = json.load(json_file)
        print("\n1. Start The Game")
        print("2. Show LeaderBoard")
        print("3. Exit the Game\n")
        option = int(input("Enter the Choice: "))
        if option == 3:
            print("! Thanks for Playing !")
            break
        elif option == 2:
            display(leaderboard)
        elif option == 1:
            startgame()