import random
class Hangman:
    def __init__(self,word_list,num_lives = 5):                   
        self.word = random.choice(word_list)                      
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(self.word_guessed)
        self.num_lives = 5
        self.word_list = ["apple", "orange", "pear", "blackberries", "strawberries"]
        self.list_of_guesses = []

    def check_guess(self, guess):                     
        guess_lowercase = guess.lower()          
        guess = guess_lowercase                  
        print(guess)
        if guess in self.word:
         print("Good guess!" ,guess, ",is in the word.")
         for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = letter
                print(' '.join(self.word_guessed))
                break
            self.num_letters -= 1
        else:
             self.num_lives = self.num_lives - 1
             print("Sorry," ,guess, "is not in the word.")
             print("You have," ,self.num_lives, "lives left.")
        
        
        
        
    def ask_for_input(self):                        
        list_of_guesses = list()               
                          
        guess = input('Please choose a letter: ') 
        if len(guess) == 2:                      
         print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
         print("You already tried that letter!")
        else:
          self.list_of_guesses.append(guess)
          hangman.check_guess(guess)
               

    def play_game(self, word_list):
        num_lives = 5
        game = Hangman(self.word_list,self.num_lives)
        while True:
                if self.num_lives == 0:
                    print('You lost!')
                    break
                elif self.num_letters > 0:
                   hangman.ask_for_input()
                elif self.num_lives > 0 and self.num_letters == 0:
                    print('Congratulations. You won the game!')
                    break 
hangman = Hangman(["apple", "orange", "pear", "blackberries", "strawberries"])
hangman.play_game(["apple", "orange", "pear", "blackberries", "strawberries"])  


print(hangman.list_of_guesses)
print(hangman.word_guessed)
print(hangman.num_letters)