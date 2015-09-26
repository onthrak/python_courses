# template for "Stopwatch: The Game"
import simplegui
import time


# define global variables
clock = 0
x = 0
y = 0
d = 0
b = 0
eb = 0 ## for b
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(clock):
    global b, d
    """ last 3 numbers,
    seconds and tenth of second """
    a = clock // 600 # a is alright, minutes
    bc = clock // 10 ## it is important
    c = str(bc)[-1] # c is alright, seconds
    #b is bad, second * 10
    d = abs(bc * 10 - clock) # d is alright, tenth of sec
   
    return str(a)+":"+str(b)+c+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startb():
    global timer, timb
    timer.start()
    timb.start()

def stopb():
    global x,y,d,b
    global timer, timb
    if timer.is_running():
        if d == 0:
            x +=1
    if timer.is_running():
        y +=1
    
    timer.stop()
    timb.stop()
def resetb():
    global x,y,d,b, eb
    x = 0
    y = 0
    d = 0
    b = 0
    eb = 0
    global timer, timb
    timer.stop()
    timb.stop()
    global clock
    clock = 0


    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global clock
    clock += 1
    
""" special event handler for b, because im too stupid too    
figure out how extract seconds from clock :D """

def timerb():
    global eb ## for b
    global b
    eb += 1
    if eb == 100:
        if b == 5:
            b = 0
            eb = 0
        else:
            b += 1
            eb = 0
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(clock), [50,170], 64, "White")
    canvas.draw_text(str(x)+" / "+str(y), [150,100], 36, "Green")
    
# create frame
f = simplegui.create_frame("Stopwatch",300,300)

# create timer
timer = simplegui.create_timer(100, timer_handler)
timb = simplegui.create_timer(100, timerb)

# register event handlers
f.add_button("Start", startb, 150)
f.add_button("Stop", stopb, 150)
f.add_button("Reset", resetb, 150)
f.set_draw_handler(draw)
# start frame
f.start()

# Please remember to review the grading rubric
