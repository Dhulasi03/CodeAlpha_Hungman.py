import random

# List of predefined words
words = ["apple", "banana", "grape", "mango", "peach"]

# Randomly choose a word
word = random.choice(words)
guessed_word = ["_"] * len(word)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game")
print("You have 6 incorrect attempts to guess the word.")

while attempts > 0 and "_" in guessed_word:
    print("\nCurrent Word: " + " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for index in range(len(word)):
            if word[index] == guess:
                guessed_word[index] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over. The word was:", word)
