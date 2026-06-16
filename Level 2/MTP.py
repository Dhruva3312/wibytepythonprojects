# Simple Word Guessing Game

# BONUS IDEA: Importing 'random' lets the computer pick a surprise word from our list.
import random

def main():
    # Say hello and explain the game rules simply
    print("-----------------------------------------")
    print("      WELCOME TO THE WORD GUESS GAME     ")
    print("-----------------------------------------")
    print("I will pick a secret word, and you try to guess it!")
    
    # Our list of secret words
    word_list = ["apple", "banana", "cookie", "guitar", "sunset"]
    
    # Get the player's name
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}! Let's start.\n")

    # This variable keeps the game running as long as the player wants
    keep_playing = "yes"

    while keep_playing == "yes" or keep_playing == "y":
        
        # BONUS IDEA: Using random.choice picks a random word so the game is different every time.
        secret_word = random.choice(word_list)
        
        # SLICING: Grab the first 2 letters and the last letter to give the player a hint
        hint_start = secret_word[:2]
        hint_end = secret_word[-1]
        
        print(f"HINT: The word starts with '{hint_start}' and ends with '{hint_end}'.")
        print(f"The word has {len(secret_word)} letters.")
        
        # Get the user's guess
        guess = input("What is your guess? ")
        
        # IF-ELIF-ELSE: Check if the user got it right, left it blank, or missed it
        if guess.lower() == secret_word:
            print("Great job! You got it right! 🎉")
            
        elif guess == "":
            print("It looks like you didn't type anything!")
            
        else:
            print(f"Not quite! The correct word was: {secret_word}")
        
        # Ask if they want to play again
        print("-----------------------------------------")
        keep_playing = input("Do you want to play again? (yes/no): ")
        keep_playing = keep_playing.lower()
        
        # BONUS IDEA: .isalpha() checks if the user typed normal letters instead of numbers or symbols.
        if not keep_playing.isalpha():
            print("I didn't quite catch that, so I will close the game.")

    # Say goodbye when the loop ends
    print(f"\nThanks for playing, {name}! Have a great day!")

# This tells Python to run our game
if __name__ == "__main__":
    main()