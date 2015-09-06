### Rock-paper-scissors-lizard-Spock game


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - "rock"
# 1 - "Spock"
# 2 - "paper"
# 3 - "lizard"
# 4 - "scissors"
import random
# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        number=0
        return number
    elif name == "Spock":
        number=1
        return number
    elif name == "paper":
        number=2
        return number
    elif name == "lizard":
        number=3
        return number
    elif name == "scissors":
        number=4
        return number
    else:
        print "invalid name: "+name
    

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name="rock"
        return name
    elif number == 1:
        name="Spock"
        return name
    elif number == 2:
        name="paper"
        return name
    elif number == 3:
        name="lizard"
        return name
    elif number == 4:
        name="scissors"
        return name
    else:
        print "invalid num"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    player_number=name_to_number(player_choice) 
    comp_number=random.randrange(0,5)
    ## computer choice from number 0 -4 
    comp_choice=number_to_name(comp_number) 
    hum="Player"  ### he is second
    comp="Computer" ### he is first
    result=(comp_number-player_number) % 5
    if result == 1 or result == 2:
        message="Computer wins!"
    elif result==0:
        message="Player and computer tie!"
    else:
        message="Player wins!"
        
        
    print hum+" chooses "+player_choice
    print comp+" chooses "+comp_choice
    print message
    print "                                   "
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


