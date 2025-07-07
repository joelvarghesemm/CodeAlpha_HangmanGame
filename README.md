import random

# Step 1: Define a small list of 5 words
word_list = ["apple", "banana", "cherry", "grape", "orange"]

# Step 2: Randomly select a word
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Step 3: Display game intro
print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_incorrect, "lives.")

# Step 4: Game loop
while incorrect_guesses < max_incorrect:
    # Show the current word with guessed letters
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("\nWord:", display_word)
    
    # Check if word is fully guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # Ask the user for a guess
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess! Lives left:", max_incorrect - incorrect_guesses)

# Step 5: Game over condition
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over! The word was:", secret_word)
