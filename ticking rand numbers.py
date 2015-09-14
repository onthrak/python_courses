# Example of a simple event-driven program

# CodeSkulptor GUI module
import simplegui
import random

# Event handler
def tick():
    print random.randint(0,10)

# Register handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
