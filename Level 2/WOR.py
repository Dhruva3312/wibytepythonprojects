import random
import tkinter as tk
from tkinter import messagebox

# Track number of guesses made
guessnum = 0


def show_answer():
  """Displays the correct word in a popup dialog."""
  messagebox.showinfo(
      "Help", f"The hidden word is: {chosenWord.upper()}"
  )


def getWord():
  global guessnum

  # Check if maximum guesses (6 attempts) have been reached
  if guessnum >= 6:
    messagebox.showwarning(
        "Game Over", f"No more guesses left! The word was: {chosenWord.upper()}"
    )
    return

  # Format input: strip whitespace and convert to lowercase
  guessedWord = EntryBox.get().strip().lower()

  # Ensure the entry is exactly 5 letters long
  if len(guessedWord) != 5:
    messagebox.showwarning("Warning", "Please enter a 5-letter word.")
    return

  if guessedWord in wordlist:
    # Track letter frequencies in the secret word to correctly color duplicate letters
    chosen_counts = {}
    for char in chosenWord:
      chosen_counts[char] = chosen_counts.get(char, 0) + 1

    letter_colors = ['grey'] * 5

    # First Pass: Find exact positional matches (Green)
    for kk in range(5):
      if guessedWord[kk] == chosenWord[kk]:
        letter_colors[kk] = 'green'
        chosen_counts[guessedWord[kk]] -= 1

    # Second Pass: Find wrong-position matches (Gold) using remaining counts
    for kk in range(5):
      if letter_colors[kk] != 'green':
        char = guessedWord[kk]
        if char in chosen_counts and chosen_counts[char] > 0:
          letter_colors[kk] = 'gold'
          chosen_counts[char] -= 1

    # Render row labels with determined colors
    for kk in range(5):
      label = tk.Label(
          window,
          text=guessedWord[kk].upper(),
          font=('Helvetica', 14, 'bold'),
          bg=letter_colors[kk],
          fg='white',
          borderwidth=1,
          relief='solid',
          width=4,
          height=2,
      )
      label.grid(row=guessnum, column=kk, padx=2, pady=2, sticky=tk.NSEW)

    guessnum += 1
    EntryBox.delete(0, tk.END)  # Clear the input field for the next guess

    # Check win/loss outcomes
    if guessedWord == chosenWord:
      messagebox.showinfo(
          "Congratulations!",
          f"You guessed the word in {guessnum} attempt(s)!",
      )
      GuessButton.config(state='disabled')
    elif guessnum == 6:
      messagebox.showinfo(
          "Game Over", f"Out of guesses! The correct word was: {chosenWord.upper()}"
      )
      GuessButton.config(state='disabled')

  else:
    messagebox.showerror(
        "Invalid Word", "Word not found in wordlist. Please try again."
    )


# Read words file and convert all entries to clean lowercase
with open('5_letter_words.txt') as file:
  words = file.read()

wordlist = [word.strip().lower() for word in words.splitlines() if word.strip()]
chosenWord = random.choice(wordlist)

# GUI Setup
window = tk.Tk()
window.title("Wordle")
window.geometry("320x420")

# Input field across the grid footer
EntryBox = tk.Entry(window, font=('Helvetica', 12))
EntryBox.grid(
    row=99, column=0, columnspan=5, pady=(20, 5), padx=10, sticky='ew'
)

# Action Buttons
GuessButton = tk.Button(
    window, text="Guess", command=getWord, font=('Helvetica', 10, 'bold')
)
GuessButton.grid(row=100, column=0, columnspan=3, pady=5, padx=5, sticky='ew')

HelpButton = tk.Button(
    window, text="Reveal Answer", command=show_answer, font=('Helvetica', 10)
)
HelpButton.grid(row=100, column=3, columnspan=2, pady=5, padx=5, sticky='ew')

# Bind Enter key to trigger guess
window.bind('<Return>', lambda event: getWord())

window.mainloop()