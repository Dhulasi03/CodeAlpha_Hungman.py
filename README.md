 
# CodeAlpha - Hangman Game

## ✅ Project Title:
**Hangman Game (Text-Based)**

## 📌 Task Description:
This is a classic Hangman game implemented in Python. The user attempts to guess a hidden word one letter at a time within a limited number of incorrect attempts.

## 💡 Features:
- Randomly selects a word from a predefined list.
- Limits the user to 6 incorrect guesses.
- Displays the word progress and used letters.

## 🧠 Concepts Used:
- `random` module
- `while` loop, `if-else`
- `lists`, `strings`
- User input handling
## Sample Output:
 
 Welcome to Hangman Game
You have 6 incorrect attempts to guess the word.

Current Word: _ _ _ _ _
Enter a letter: m
Correct guess!

Current Word: m _ _ _ _
Enter a letter: a
Correct guess!

Current Word: m a _ _ _
Enter a letter: n
Correct guess!

Current Word: m a n _ _
Enter a letter: g
Correct guess!

Current Word: m a n g _
Enter a letter: t
Wrong guess. Attempts left: 5

Current Word: m a n g _
Enter a letter: r
Wrong guess. Attempts left: 4

Current Word: m a n g _
Enter a letter: d
Wrong guess. Attempts left: 3

Current Word: m a n g _
Enter a letter: o
Correct guess!

Congratulations! You guessed the word: mango

