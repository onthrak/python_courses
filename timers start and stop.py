import simpleguitk
import time
x=1

def timer_handler():
    global x
    x+=4
    print x
    print time.time()
    print ""
    global timer
    if x >=16:
        timer.stop()
        timer = simpleguitk.create_timer(500, timer_handler)
        timer.start()
timer = simpleguitk.create_timer(1000, timer_handler)
timer.start()

