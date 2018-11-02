"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

I am trying for an exceeds rating but if it falls short thats ok.
"""
import random

def start_game():
    """
    3. Display Highscore that persists until application quit
    """
    # write your code inside this function.
    print("Hi, Welcome to the Guessing Game!\n")
    # initializing the variables for the loop
    attempts = 0

    guess = 0

    the_number = random.randint(1,10)

    high_score = 0

    # the main loop
    while True:
        # error checking
        try:
            # checks to make sure there is a high score then displays it
            if high_score != 0:
                print("High Score: ", high_score)
            else:
                pass
            # takes in players guess
            guess = int(input("Make a guess between 1 and 10: "))

            # increments attempts by one to track guesses
            attempts += 1

            # main decision filter
            if guess > 10 or guess < 1:
                print("That guess is outside of the range\n")
                # decrements by one on a bad attempt
                attempts -= 1
            elif guess > the_number:
                print("It's lower\n")
            elif guess < the_number:
                print("It's higher\n")
            # ends the round if the players guesses the number
            elif guess == the_number:
                print("Got it\n")
                print("It took you {} attempts !".format(attempts))                      
                print("************ROUND OVER************\n")
            
        except ValueError or TypeError:
            print(" Sorry that was not a valid entry please try again\n")

        # checks to see if the game is over and if you want to keep playing
        if guess == the_number:
            # error checking for input
            try:
                keep_playing = str(input("Would you like to keep playing? "
                                                         "Type Y for yes or anything else for no: "))
                # if yes to continue
                if keep_playing.lower() == 'y':
                    # resets the number to guess
                    the_number = random.randint(1,10)
                    if high_score == 0 or attempts < high_score:
                        # sets the high score
                        high_score = attempts
                    else:
                        pass
                    # resets the attempts variable
                    attempts = 0
                    continue
                # if no to continue
                else:
                    return print("\n************GAME OVER Thanks for playing************")
                
            except ValueError or TypeError:
                print(" Sorry that was not a valid entry please try again")
        else:
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
