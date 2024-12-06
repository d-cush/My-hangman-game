import tkinter as tk
import random

# Function to choose a random word from the word list
def choose_word():
    """Chooses a random word from a predefined list of words."""
    words = [
        "python", "programming", "hangman", "developer", "algorithm", "apple", "computer",
        "lights", "canvas", "banana", "car", "dog", "elephant", "fish", "grape", "house",
        "igloo", "jacket", "kite", "lemon", "monkey", "night", "orange", "penguin", "queen",
        "rose", "sun", "tree", "umbrella", "vase", "water", "xylophone", "yellow", "zebra"
    ]
    sw = random.choice(words)  # sw = secret word
    print(f"Secret word: {sw}")  # Debugging: Prints the chosen word to the console
    return sw

# Function to start a new game
def start_game():
    """Initializes or resets the game state for a new round."""
    global word, word_letters, guesses_left, guessed_letters
    word = choose_word()  # Select a new secret word
    word_letters = set(word)  # Unique letters in the word
    guesses_left = 6  # Maximum allowed incorrect guesses
    guessed_letters = set()  # Track player's guessed letters
    canvas.delete("all")  # Clear the canvas for a new game
    draw_hangman(guesses_left)  # Draw initial hangman structure
    update_display()  # Update word and guess displays

# Function to handle player's letter guesses
def guess_letter(letter):
    """Handles the player's guessed letter and updates the game state."""
    global guesses_left, guessed_letters

    # Skip processing if letter has already been guessed or game is over
    if letter in guessed_letters or guesses_left == 0:
        return

    guessed_letters.add(letter)  # Add letter to guessed set

    # Check if the guessed letter is incorrect
    if letter not in word_letters:
        guesses_left -= 1  # Decrease remaining guesses
        draw_hangman(guesses_left)  # Update the hangman drawing

    update_display()  # Update the displayed word and status

# Function to update the displayed word and game status
def update_display():
    """Updates the word display, remaining guesses, and result messages."""
    word_label.config(
        text=" ".join([letter if letter in guessed_letters else "_" for letter in word])
    )  # Show guessed letters or underscores

    guesses_label.config(text=f"Guesses left: {guesses_left}")  # Update guesses left

    # Check for game outcome
    if guesses_left == 0:
        result_label.config(text=f"You lost! The word was: {word}", fg="red")
    elif word_letters.issubset(guessed_letters):
        result_label.config(text="You won!", fg="green")

# Function to draw the hangman figure based on remaining guesses
def draw_hangman(guesses):
    """Draws the hangman figure based on the number of incorrect guesses left."""
    canvas.delete("all")  # Clear previous drawings

    # Draw the gallows
    canvas.create_line(50, 200, 150, 200, width=3)  # Base
    canvas.create_line(100, 200, 100, 50, width=3)  # Vertical pole
    canvas.create_line(100, 50, 175, 50, width=3)   # Top bar
    canvas.create_line(175, 50, 175, 75, width=3)   # Rope

    # Draw parts of the hangman based on incorrect guesses
    if guesses <= 5:
        canvas.create_oval(150, 75, 200, 125, width=3)  # Head
    if guesses <= 4:
        canvas.create_line(175, 125, 175, 175, width=3)  # Body
    if guesses <= 3:
        canvas.create_line(175, 135, 150, 160, width=3)  # Left arm
    if guesses <= 2:
        canvas.create_line(175, 135, 200, 160, width=3)  # Right arm
    if guesses <= 1:
        canvas.create_line(175, 175, 150, 200, width=3)  # Left leg
    if guesses == 0:
        canvas.create_line(175, 175, 200, 200, width=3)  # Right leg

# Create the main application window
root = tk.Tk()
root.title("Hangman")

# Create and configure labels for the word, guesses, and result
word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=10)

guesses_label = tk.Label(root, text="", font=("Arial", 12))
guesses_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="red")
result_label.pack(pady=10)

# Create a canvas for drawing the hangman
canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(pady=10)

# Create a frame for the letter buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create buttons for each letter of the alphabet
for letter in "abcdefghijklmnopqrstuvwxyz":
    button = tk.Button(
        button_frame,
        text=letter,
        font=("Arial", 14),
        width=2,
        command=lambda letter=letter: guess_letter(letter)  # Pass current letter to handler
    )
    button.grid(
        row=(ord(letter) - 97) // 9,  # Determine button row
        column=(ord(letter) - 97) % 9,  # Determine button column
        padx=2, pady=2
    )

# Create a restart button to start a new game
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 12), command=start_game)
restart_button.pack(pady=10)

# Start the initial game and Tkinter main loop
start_game()
root.mainloop()







