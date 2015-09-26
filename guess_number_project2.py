# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print ""
    print "New game. Range is [0,100)"
    global num
    num=random.randrange(0,100)
    global count
    count = 7
    print "Number of remaining guesses is "+str(count)
    print ""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num
    num=random.randrange(0,1000)
    global count
    count = 10
    print ""
    print "New game. Range is [0,1000)"
    print "Number of remaining guesses is "+str(count)
    print ""

       
def input_guess(guess):
    # main game logic goes here
    global count
    if int(guess)==num:
        print "Guess was "+guess
        print "Correct!"
        new_game()
    elif int(guess)>num:
        count = count - 1
        print "Guess was "+guess
        print "Number of remaining guesses is "+str(count)
        print "Lower!"
        print ""
    else:
        count = count - 1
        print "Guess was "+guess
        print "Number of remaining guesses is "+str(count)
        print "Higher!"
        print ""
    if count == 0:
        print "You lose, hahaha"
        new_game()
        
    

# create frame
f = simplegui.create_frame("Guess the number",200,200)
f.add_button("Range is [0,100)", range100, 100)
f.add_button("Range is [0,1000)", range1000, 100)
f.add_input("Enter a guess", input_guess, 100)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
