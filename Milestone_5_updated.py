import random


class Hangman:
    '''This class is used to represent the Hangman game.

    Attributes:
    word (str): A random word selected from the word_list.
    word_guessed (str): A list of underscores which replace the letters in the word.
    num_letters (int): The length of the randomly selected word. 
    num_lives (int): The number of lives a player has at the start of the game.
    word_list (str): A list of possible words that could be randomly selected.
    list_of_guesses (str): A list of guesses that a player has made throughout the game. 
    '''
    
    def __init__(self, word_list, num_lives = 5): 
        self.word = random.choice(word_list)                      
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = 5
        self.word_list = word_list
        self.list_of_guesses = []
        '''See help(Hangman) for accurate signature.'''
        


    def check_guess(self, guess): 
        '''This function is used to convert guess into lowercase letters and checks the guess to see if the guess is in the word.

        prints:
         str: The word_gussesed list is printed with the correct guessed letters in the list and it also subtarcts the number of correct guess from num_letters. 
         str: The message sorry guess is not in word is print if guess is incorrect and it reduces the players lives by one. 
        '''

        guess_lowercase = guess.lower()          
        guess = guess_lowercase                  
        print(guess)
        if guess in self.word:
            print("Good guess!" , guess , ",is in the word.")
            for index, letter in enumerate(self.word):
                    if letter == guess:
                        self.word_guessed[index] = letter
            print(' '.join(self.word_guessed))
            self.num_letters -= 1
        else:
             self.num_lives = self.num_lives - 1
             print("Sorry," ,guess, "is not in the word.")
             print("You have," ,self.num_lives, "lives left.")
        
        
        
        
    def ask_for_input(self): 
        '''This function checks that the guess is an valid guess based on the conditions set in the if statement.

        prints:
        str: Please enter choose a letter, if guess is vaild it will check to see if guess is in word and append it to list_of_guesses.
        str: If guess is not vaild it will print invaid guess or if you try the same letter again it will print that you already tried that letter.
        '''                      
        list_of_guesses = list()               
                          
        guess = input('Please choose a letter: ') 
        if guess.isalpha() and len(guess) is not 1:                        
         print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
         print("You already tried that letter!")
        else:
          self.list_of_guesses.append(guess)
          self.check_guess(guess)

def play_game(word_list):
    '''This function is used to start the game and it uses if and elif statements to check to see if you win or lose.

    prints:
    str: it will print you lose if you use all your lives or it will print you win if you have lives remaining and guessed all the misiing letters.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:


        if game.num_lives == 0:
         print('You lost!')
         break
        elif game.num_letters > 0:
         game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
         print('Congratulations. You won the game!')
         break 
if __name__=='__main__':
    play_game(["apple", "orange", "pear", "blackberries", "strawberries"]) 

