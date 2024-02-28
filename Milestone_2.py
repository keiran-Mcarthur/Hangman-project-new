import random 
# add functions
word_list = ["apple", "orange", "pear", "blackberries", "strawberries"]
word = random.choice(word_list)
print(word)

# add functions
guess = input('Please choose a letter: ')
print(guess)

# add functions
if len(guess) == 1:
    print("Good Guess")
else:
    print("Oops! That is not a valid input.")

