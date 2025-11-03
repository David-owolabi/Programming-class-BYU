"""import random

play_again = 'yes'

while play_again == 'yes':
    magic = random.randint(1, 100)
    guess = None
    count = 0

    while guess != magic:
        guess_input = input("What is your guess? ")
        guess = int(guess_input)
        count += 1

        if guess < magic:
            print("Higher")
        elif guess > magic:
            print("Lower")
        else:
            print(f"You guessed it in {count} tries!")

    play_again = input("Would you like to play again (yes/no)? ").lower()"""


    #strech challenge

import random

def play_game():
    magic = random.randint(1, 100)
    guess = None
    count = 0

    print("\nWelcome to the Guess My Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while guess != magic:
        try:
            guess_input = input("\nWhat is your guess? ")
            guess = int(guess_input)
            count += 1

            if guess < magic:
                print("Higher")
            elif guess > magic:
                print("Lower")
            else:
                print(f"\nCongratulations! You guessed it in {count} tries!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ")

    print("\nThanks for playing! Goodbye.")

if __name__ == "__main__":
    main()