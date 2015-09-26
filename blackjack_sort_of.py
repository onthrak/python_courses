##### blackjack (sort of)
values=1,2,3,4,5,6,7,8,9,10,10,10,10,1
names=('1','2','3','4','5','6','7','8','9','10','J','D','K','A')
 ##test blackjack
"""
for x in range (0, len(names)):
    print ""
    print values[x]
    print names[x]
    print ""
"""


import math
import random
import simplegui
#x= random.choice(values)


def new_game():
    print ""
    global total 
    total = 0
    global comp_total
    comp_total = 0
    print "Start new game"

    
### button handlers

def more():
    print ""
    global total
    global comp_total
    x = random.choice(values)
    total = total + x
    if comp_total <= 17:
        y = random.choice(values)
        comp_total = comp_total + y
        print "Dealer get: "+ names[y-1]
    print "You get: "+ names[x-1]
    print "Now you have total value equal: "+str(total)
    print "Dealer have total value equal: "+str(comp_total)
    if total > 21 and comp_total < 21:
        print "You LOSE!"
        new_game()
    elif comp_total > 21:
        print "You WIN!"
        new_game()
    elif total > 21 and comp_total > 21:
        if total < comp_total:
            print "You WIN!"
            new_game()
        elif total > comp_total:
            print "You LOSE!"
            new_game()
        else:
            print "TIE!!"
            new_game()
        
    print ""
def save():
    print ""
    print "Now you have total value equal: "+str(total)
    global comp_total
    # print str(comp_total)
    while comp_total <= 17:
        y = random.choice(values)
        comp_total = comp_total + y
        print "Dealer have total value equal: "+str(comp_total)
        
    if total>comp_total:
        
        print "You WIN!"
        new_game()
    elif total<comp_total:
        
        print "You LOSE!"
        new_game()
    else:
        print "TIE!!"
        new_game()

### frame

f = simplegui.create_frame("Blackjack", 200, 200)
f.add_button("Add next card", more, 100)
f.add_button("Check", save, 100)

### start frame

f.start()

### start game

new_game()

        
    
