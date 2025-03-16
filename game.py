#CMSC 12 Project: Hangman 
'''
Adrian B. Cueto
2020-02461
BS Computer Science
'''


import random #this will be used to randomize the words
#this will import all dictionaries to be used in selecting the word
from dictionary import *

def Game(word, points, difficulty):  #this will run the game
    display_word = "-" * len(word) #this will serve as the empty word that will be filled 
    guessed = False  #this is the statement to identify if the word was already guessed, also a counter for the while loop
    tried_letters = [] #the tried letters will be placed here to avoid repetition
    tried_words = [] #same above but with words instead
    tries = 6 #this serves as the tries for guessing the word
    
    print(Hangman(tries)) #this will print the stick figure in the game
    print(display_word + "\n") #this will show the blank word
    print("The word has", len(word), "letters.") #this will show how many letters does the word have
    
    while not guessed and tries > 0: #this while loop serves as the turns of the games
        guess = input("Guess a letter or word: ").upper() #.upper() is used so that the input will be uppercased
        if len(guess) == 1 and guess.isalpha():	#condition to determine if the input is valid and a letter
            if guess in tried_letters:		#determine if the letter was already selected
                print("You already guessed the letter", guess) 
            
            elif guess not in word:  #determine if the letter is not in the word
                print(guess, "is not in the word.")
                tries -= 1
                tried_letters.append(guess)
            
            else: #if the letter is in the word
                print("Good job!", guess, "is in the word")
                tried_letters.append(guess) #this will add letters to the guess
                word_as_list = list(display_word) #the word will become a list
                indices = [i for i, letter in enumerate(word) if letter == guess] #this creates the index of the letters in the word if the letter is guessed
                for index in indices: 
                    word_as_list[index] = guess #this will change the blank ("-") symbol to the letter guessed
                display_word = "".join(word_as_list) #this will become a string
                if "-" not in display_word: #if this was satisfied, the game is finished
                    guessed = True
        
        elif len(guess) == len(word) and guess.isalpha():  #condition to determine if the input is valid and a word.
            if guess in tried_words: 	#if guess is already selected
                print("You already guessed the word", guess)
            elif guess != word: #if guess is not the word
                print(guess, "is not the word.")
                input()
                tries -= 1
                tried_words.append(guess)
            
            else: #if the word guessed is correct
                guessed = True
                display_word = word
        
        else:
            print("Not a valid guess.")
        #this shows the hangman and the incomplete word
        print(Hangman(tries))
        print(display_word + "\n")

    if guessed: #this will show if the word is guessed
        print("Congrats! you have guessed the word!")
        if difficulty == 1:
        	points += 1
        elif difficulty == 2:
        	points += 3
        elif difficulty == 3:
        	points += 5
    else: #this is showed if the word was not guessed within those trials
        print("Sorry, you ran out of tries. The word was " + word + ".")

    return points
    

def Hangman(tries): #this function will be used to animate the hangman game
    stages = [  # final state: head, torso, both arms, and both legs
				"""
--------
|      |
|      O
|     \\|/
|      |
|     / \\
-
                """,
                # head, torso, both arms, and one leg
                """
--------
|      |
|      O
|     \\|/
|      |
|     / 
-
                """,
                # head, torso, and both arms
				"""
--------
|      |
|      O
|     \\|/
|      |
|      
-
                """,
                # head, torso, and one arm
                """
--------
|      |
|      O
|     \\|
|      |
|     
-
                """,
                # head and torso
                """
--------
|      |
|      O
|      |
|      |
|     
-
                """,
                # head
                """
--------
|      |
|      O
|    
|      
|     
-
                """,
                # initial empty state
                """
--------
|      |
|      
|    
|      
|     
-
                """
    ]

    return stages[tries] #this will index the list so that the hangman will also change depending on the tries left

def MainMenu(points): #this is the menu and welcome screen
	print("""
$$\   $$\                                                                 
$$ |  $$ |                                                                
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  
$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ 
$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |
\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|
                              $$\   $$ |                                  
                              \$$$$$$  |                                  
                               \______/                                   
""")
	input("Press Enter to start the game.\n") 
	category = int(input('''Choose a category: 

[1] Animals
[2] Colors
[3] Appliances
[4] Countries
[5] Python Functions 

INPUT: '''))

	difficulty = int(input('''Choose a difficulty: 

[1] Easy (1 point per correct answer)
[2] Medium (3 points per correct answer)
[3] Hard  (5 points per correct answer)

INPUT: '''))

	word = GetWord(category, difficulty) #this function call is used to get the word
	HighScore(Game(word, points, difficulty)) #this will start the game


def GetWord(category, difficulty):
	word_list = ChooseDifficulty(ChooseCategory(category), difficulty)
	word = random.choice(word_list)
	
	return word.upper()

def ChooseCategory(category): #this will determine the dictionary to be used 
	if category == 1:
		return Animals
	elif category == 2:
		return Colors	
	elif category == 3:
		return Appliances
	elif category == 4:
		return Countries
	elif category == 5:
		return PythonFunctions

def ChooseDifficulty(category, difficulty): #this will determine the list to be randomized
	if difficulty == 1:
		return category["Easy"]
	elif difficulty == 2:
		return category["Medium"]
	elif difficulty == 3:
		return category["Hard"]

def HighScore(points): #this is the high score function
	print("Your current point/s is:", points) #current points are shown here

	fileHandle = open("highscore.txt", "r") #this will open the highscore.txt
	for line in fileHandle:
		highscore_list = line[:-1].split(" ") #this will put the current highscore in the list
	fileHandle.close()

	if points > int(highscore_list[0]): #if the highscore is beaten
		highscore_list[0] = points
		print("YOU GOT THE NEW HIGH SCORE!")
		fileHandle = open("highscore.txt", "w")
		for score in highscore_list:
			fileHandle.write(str(score) + "\n")
		fileHandle.close()
	else: #if the highscore was not beaten
		print("The current highscore is:", highscore_list[0])

	RepeatGame(points) #this will call the final function

def RepeatGame(points): #this is the function to repeat the whole game:
	question = input("Continue? Y/N: ")
	if question.upper() == "Y":
		MainMenu(points)
	else:
		print("\n\nCreated by: Adrian B. Cueto BSCS")
		exit()

points = 0
MainMenu(points) #this is the main function call