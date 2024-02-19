import random 
# add functions
word_list = ["apple", "orange", "pear", "blackberries", "strawberries"]
print(random.choice(word_list))
word = 'orange'
print(word)
# add functions
guess = input('Please choose a letter: ')
print(guess)
# add functions
if len(guess) == 1:
    print("Good Guess")
else:
    print("Oops! That is not a valid input.")

if "guess" in word:
    print("Good guess!" ,guess, "is in the word.")
else:
    print("Sorry," ,guess, "is not in the word. Try again.")