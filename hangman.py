import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
# Function shows user menu
def show_menu():
    cls()
    print("Welcome to the Hangman game!")
    print("You can choose three levels of difficulty:")
    print("type in \"easy\" - you have 7 tries and word-pool is Europe.") 
    print ("type in \"medium\" - you have 5 tries and game will be played in both Americas' and Australia as extra") 
    print("type in \"hard\"  - you have 3 tries and your guess is from among Africa, Asia")
    print ("\n\n If you want to leave the game type \"quit\"")
# Function loads capitals and countries from file 
def load_set_from_file (filename):
    try:
        f = open(filename,"rt",  encoding="utf8",)
    except:
        print("Problem occured!")
    else:
        #my_set = f.readlines()
        
        #  loads lines to set
        easy_set = set()
        medium_set = set()
        hard_set = set()

        is_end_of_file = False
        while not is_end_of_file: 
        
            line = f.readline()
            if "easy" in line:
                easy_set.add(line)
            elif "medium" in line:
                medium_set.add(line)
            elif "hard" in line:
                hard_set.add(line)
            if len(line) == 0:
                is_end_of_file = True
        
        f.close()
        return ([easy_set, medium_set, hard_set])
        
# Function draws and returns list of [word_to_guess, hint, continent]    
def draw_word_to_guess(my_set):

    #   draws line from set
    drawn_line = random.choice(tuple(my_set))
    #print(drawn_line)
    
    #   draws country or capital from line and returns it with hint and continent
    line_to_guess = drawn_line.split("\t")
                            #could be (but we changed it on purpose): word_to_guess = random.choice([line_to_guess[0],line_to_guess[1]])
    capital_or_country = random.randint(0,1)
    if capital_or_country == 0:
        word_to_guess = line_to_guess[0]
        hint = line_to_guess[1]
    else:
        word_to_guess = line_to_guess[1]
        hint = line_to_guess[0]

    continent = line_to_guess[2].splitlines(0)

    # print([word_to_guess,hint,continent])
    return([word_to_guess,hint,continent[0]])
def show_hint(my_set):
    print("Hint: "+ str(my_set[1]) + " (" + str(my_set[2]) + ")")
    # print (f"Hint: {my_set[1]} ({my_set[2]})")   
# Function displays number of lives 
def show_lives(user_guess, lives_left, difficulty_level):

    # #if user_guess
    # lives_left = lives_left 
    # print(lives_left * '[]')
    # lives_left -= 1
    cls()
    print ("Hangman game:")
    print ("\nLeft lives: " + lives_left * '[]'+ (difficulty_level - lives_left) * '[X]')
    print ("Your current progress: " + " ".join(user_guess))
def play (word_to_guess_hint_continent, lives):

    word_to_guess = word_to_guess_hint_continent[0]
    #word_to_guess = "Warsaw Warsaw"
    #hint = word_to_guess_hint_continent[1]
    #continent = word_to_guess_hint_continent[2]

    lives_left = lives
    user_guess = (len(word_to_guess) * "_ ").split()
   


    for letter_index_in_word in range(len(word_to_guess)):
        if word_to_guess[letter_index_in_word]  == " ":
            # if letter in guessed word is the same as letter guessed by user then we take letter from original word to guessed (letter) word
            user_guess[letter_index_in_word] = word_to_guess[letter_index_in_word]


    #print(user_guess)
    
    is_guess_correct = False
    user_wants_play = True
    while (lives_left > 0 and not is_guess_correct and user_wants_play):
        print("Type in letter or word / quit - if you want")
        try:
            show_lives(user_guess,lives_left,lives)   
            show_hint(word_to_guess_hint_continent)
            guess = input("Your guess: ")
            # print (guess)
            # cls()
            # checks user input and calls function show_lives
            if len(guess) == 1:

                letter = guess
                # check for each letter in word to guess if letter guessed by user is the same (Capital is not important)
                for letter_index_in_word in range(len(word_to_guess)):
                    if word_to_guess[letter_index_in_word].lower() == letter.lower():
                        # if letter in guessed word is the same as letter guessed by user then we take letter from original word to guessed (letter) word
                        user_guess[letter_index_in_word] = word_to_guess[letter_index_in_word]
                        print(f"You guessed correctly! \"{letter}\" is in a word.")
                if not (letter.lower() in word_to_guess.lower()):
                    print("Try again!")
                    lives_left -= 1


            elif guess == "quit":
                user_wants_play = False
            elif len(guess) == len(word_to_guess):
                word_to_guess == "".join(user_guess)  
                show_lives(user_guess,lives_left,lives) 
                    
                print ("Congratulations! You won!")
                input("Press any key to continue..")
                is_guess_correct = True
            else:
                print("Words aren't the same lenght! Guess again.")
                lives_left -= 1

            
            if word_to_guess == "".join(user_guess):

                show_lives(user_guess,lives_left,lives)
                print ("You won!")
                is_guess_correct = True
                
        


            
        except:
            print("Error: Wrong input. Probably too much data")
def main():
    # loads 3 sets - 3 difficulty levels into list [[easy],[medium],[hard]]
    countries_and_capitals = load_set_from_file("countries-and-capitals.txt")



    # difficulty levels:
    easy = 7
    medium = 5
    hard = 3
    
    # play(word_to_guess[0],3)
    user_wants_play = True
    while (user_wants_play):
        show_menu()

        # user chooses game level
        
        chosen_level = input("Enter chosen game level: ")
        if chosen_level == "easy" :
            print(" You chose level easy")
            # countries_and_capitals[0] == easy_set
            word_to_guess = draw_word_to_guess(countries_and_capitals[0])
            #print(word_to_guess)
            play(word_to_guess,easy)

                
        elif chosen_level == "medium":
            print (" You chose level medium - be prepared for the surprise!") 
            # countries_and_capitals[1] == medium_set
            word_to_guess = draw_word_to_guess(countries_and_capitals[1])
            #print(word_to_guess) 
            play(word_to_guess,medium)
            
        elif chosen_level == "hard":
            print ("You chose level hard - good luck! \n You'll need it ;) ")
            # countries_and_capitals[2] == hard_set
            word_to_guess = draw_word_to_guess(countries_and_capitals[2])
            #print(word_to_guess)
            play(word_to_guess, hard)
            

        elif chosen_level == "quit":
            input ("Ok! You're leaving the game. Press any key to exit.")
            user_wants_play = False
            
            
        else: 
            print ("You did not choose level. Enter valid input")
            input()



    
if __name__ == "__main__":
    main()
   
