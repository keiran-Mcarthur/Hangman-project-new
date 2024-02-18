import random 
word_list = ["apple", "orange", "pear", "blackberries", "strawberries"]
word = random.choice(word_list)
print(word)

guess = input('Please choose a letter: ')
print(guess)

if len(guess) == 1:
    print("Good Guess")
else:
    print("Oops! That is not a valid input.")
    