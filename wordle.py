import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial"]
hidden_word = random.choice(word_list)

print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""
    if len(guess_word) == 5:
        print ("-")
    else:
        print("Please use a five letter word.")
        break
    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    # Second letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    # Third letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    # Fourth letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    # Fifth letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
if len(guess_word) == 6:
    print ("please use a five letter word!")
if len(guess_word) == 7:
    print ("please use a five letter word!")
if len(guess_word) == 8:
    print ("please use a five letter word!")
