# Word Puzzle Game (Wordle-like)
# Added creativity: 
# 1. Random secret word selection from a predefined list
# 2. Maximum guess limit to increase challenge
# 3. Case-insensitive input handling

import random

def generate_hint(secret, guess):
    #Generate hint based on secret word and user's guess
    secret_lower = secret.lower()
    guess_lower = guess.lower()
    hint = []
    
    for i in range(len(secret)):
        if guess_lower[i] == secret_lower[i]:
            hint.append(guess_lower[i].upper())
        elif guess_lower[i] in secret_lower:
            hint.append(guess_lower[i].lower())
        else:
            hint.append('_')
    return ' '.join(hint)

def main():
    # Game configuration
    secret_words = ['mosiah', 'python', 'script', 'coding', 'program', 
                   'developer', 'computer', 'algorithm', 'function']
    max_guesses = 10
    secret_word = random.choice(secret_words)
    guess_count = 0
    
    print("Welcome to the word guessing game!")
    print(f"Your hint: {'_ ' * len(secret_word)}\n")

    while guess_count < max_guesses:
        guess = input("What is your guess? ").strip()
        guess_count += 1

        # Validate guess length
        if len(guess) != len(secret_word):
            print(f"❌ Guess must be {len(secret_word)} letters. Try again.\n")
            continue

        # Check for correct guess
        if guess.lower() == secret_word.lower():
            print(f"\n🎉 Congratulations! You guessed it!")
            print(f"🔢 Total guesses: {guess_count}")
            return

        # Generate and display hint
        hint = generate_hint(secret_word, guess)
        remaining = max_guesses - guess_count
        print(f"💡 Hint: {hint}")
        print(f"📊 Guesses remaining: {remaining}\n")

    # Game over if all guesses used
    print(f"⚠️ Game over! The secret word was: {secret_word.upper()}")

if __name__ == "__main__":
    main()
