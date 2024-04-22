import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def get_user_guess():

    while True:
        try:
            guess = int(input("Guess the sum of the two dice rolls (2-12): "))
            if 2 <= guess <= 12:
                return guess
            else:
                print("Please enter a number between 2 and 12.")
        except ValueError:
            print("Please enter a valid number.")

def play_dice_game():
    print("Welcome to the Dice Game!")
    while True:
        die1, die2 = roll_dice()
        user_guess = get_user_guess()
        total = die1 + die2
        print("You rolled:", die1, "and", die2)
        print("Sum of the rolls:", total)
        if user_guess == total:
            print("Congratulations! You guessed correctly!")
        else:
            print("Sorry, incorrect guess. Better luck next time!")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_dice_game()
