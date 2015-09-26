# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = 217
iteration = 0
max_iterations = 1000

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    """???  Part of mystery computation."""
    if not current % 2:
        return current / 2.0
    else:
        return (current * 3) + 1
    
# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration, result
    iteration += 1
    # Stop iterating after max_iterations
    if iteration >= max_iterations:
        timer.stop()
        print "Output is", result
    else:
        result = get_next(result)
        print result
    # Stop iterating after getting 1 
    if result == 1:
        timer.stop()
        print " Collatz ends"

# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(13)
timer.start()