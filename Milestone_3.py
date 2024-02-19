def check_guess(guess):
    lowercase = guess.lower()
    print(lowercase)
    word = 'orange'
    if guess in word:
         print("Good guess!" ,guess, "is in the word.")
    else:
         print("Sorry," ,guess, "is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input('Please choose a letter: ')
        if guess.isalpha() and 0 <= len(guess) <= 1:
            break   
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
check_guess('g')



ask_for_input()




