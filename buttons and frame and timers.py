# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 25
# Define "helper" functions
def increment():
    global counter
    counter= counter +1
# Define event handler functions
def tick():
    increment()
    print counter
def tick_ultra():
    increment()
    print counter**2
def buttonpress():
    global counter
    counter=0
    
#Create a frame
frame= simplegui.create_frame("TESTING", 200,200)
# Register event handlers
timer= simplegui.create_timer(1000, tick)
frame.add_button("Click me!", tick)
frame.add_button("RESET", buttonpress )
frame.add_button("MEGA", tick_ultra )

# Start frame and timers
frame.start()
timer.start()
