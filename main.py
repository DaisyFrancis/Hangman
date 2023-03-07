#Hangman gamne using python
import random
#importing list of words
from hangman_words import word_list 
#Generating random name from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
#total 6 lives for a player to guess the word
lives = 6 

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)


#print(f'The solution is {chosen_word}.')#for developer

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"
print("Have fun!")
while not end_of_game:
    guess = input("Guess a letter : ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")#for developers understanding
        if letter == guess:
            display[position] = letter

    #Checking if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life:(")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose :(")

    #Joining all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Checking if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Yayyy!!You win.You saved an innocent man's life.")

    #Importing the stages from hangman_art.py
    from hangman_art import stages
    print(stages[lives])