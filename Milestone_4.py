import random
class Hangman:
    def __init__(self,word_list,num_lives = 5):                   # Word_list & num_lives as parametes 
        self.word = random.choice(word_list)                      # Intialise the attributes
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(self.word_guessed)
        self.num_lives = 5
        self.word_list = ["apple", "orange", "pear", "blackberries", "strawberries"]
        self.list_of_guesses = []

    def check_guess(self, guess):                      # first method(check_guess) with guess as the parameter
        guess_lowercase = guess.lower()          # convert guess to lowercase 
        guess = guess_lowercase                  # create if statement to check if guess is in word 
        print(guess)
        if guess in self.word:
         print("Good guess!" ,guess, ",is in the word.")
         for position, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[position] = letter
                break
                
         self.num_letters = len(self.word) - 1
        else:
            self.num_lives - 1
            print("Sorry," ,guess, "is not in the word.")
            print("You have," ,self.num_lives, "lives left.")
       
    
    def ask_for_input(self):                         # seond method(ask_for_input)
        list_of_guesses = list()               # create while loop with condition True and ask user for input
        while True:                            # create if statement to check if guess is a single chara
            guess = input('Please choose a letter: ') # use elif and else to check if word already been guess 
            if len(guess) == 2:                      
             print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
             print("You already tried that letter!")
            else:
             self.list_of_guesses.append(guess)
             break         
                                                                                # task to solve problem 
hangman = Hangman(["apple", "orange", "pear", "blackberries", "strawberries"]) # created an instance of the class
hangman.check_guess('R')                                                       # used the instanced of the class to call the method
                                                                               # doing that allows us to use self. contructor in methods as we can use self as a parameter
hangman.ask_for_input()                                                        # use tab key to indent if statement inside while loop and put break at end of else statement 


print(hangman.list_of_guesses)
print(hangman.word_guessed)
print(hangman.num_letters)





