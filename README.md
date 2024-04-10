# Hangman-Project-
Hangman Project 
## Description 
This project is a digital vision of the classic game called Hangman. The aim of this project is to create a fully working hangman game that can be easliy used by anyone. The Hangman game is designed to randomly pick a word from a predefined list and the user has 5 lifes to guess the full word otherwise the lose the game. To play game simply run the name of the name of the file in the terminal to start the game. This project has taught me the importance of how you layout your code in python and having a consistent style throughtout can make it easier to identify errors even before they occur. Futhermore, this project has also taught me that planning your code can make it easier and less stressful when it comes to testing and writing your code. 

### Milestone_2.py 
This is a pushed pyhton file from the local repo that contains part 1 of the Hangman game which consists of list of possible words with a random choice selection. Followed by a user input(single character) for their guess and finally an if statement  that checks that their guess is a vaild guess. 

### Milestone_3.py
This is a pushed python file from the local repo containing the next part of the project which consists of two function. The first function checks the users guess to make sure that the guess is correct. The second function checks that the users input is a vaild guess. 

### Milestone_4.py
This is a pushed python file from the local repo that contains part_3 of the Hangman game which consists of detailed versions part_1 and 2 of the hangman game in a class which checks that the guess is in  the word and displays the length of the word with correct guess index to the right spaces. It also takes a life if you give a incorrect guess.

### Milestone_5.py
This a pushed python file which contains a final working model of the classic game of hangman.

### Milestone_5_Updated.py 
This a pushed python file which contains a checked and an updated final working model of the classic game of hangman. The structure of the model structured in using object oriented programming(OOP). The model begins with the Hangman as a class followed by a function which in an instance of the class with the following attributes: self.word, self.word_guessed, self.num_letters, self.num_lives, self.word_list, self.list_of_guess (picture 1). Within the class there are two function which are check_guess and ask_for_input which detial modified verison of Milestone_4.py. After these two function outside of the class there is another function called play_game which is used to examine if you win or lose(picture 2)

# Appendics

### Picture 1 - Class Hangman
This picture shows the Hangman class 
![hangman class](https://github.com/keiran-Mcarthur/Hangman-project-new/assets/159048029/fea64d78-4ce5-483d-9268-37996883d8c4)

### Picture 2 - Play_game function 
This image below shows the Play_game function and how it is designed to check that you win or lose  
![hangman play_game function](https://github.com/keiran-Mcarthur/Hangman-project-new/assets/159048029/ab4f6101-07b6-484c-809b-8afacdfbc821)


### Picture 3 - Hangman output 
The images below shows the ouptput when you run the code of the Hnagman game 
![hangman output](https://github.com/keiran-Mcarthur/Hangman-project-new/assets/159048029/06f27142-0ebe-491a-b664-55702772941c)
![hangman won](https://github.com/keiran-Mcarthur/Hangman-project-new/assets/159048029/1a2789a2-f0cc-4673-bbfe-b7d39fe4012a)


