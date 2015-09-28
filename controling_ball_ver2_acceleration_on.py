# Ball motion with a defined timer
# Speed of ball is increasing for every 1 second
import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0,0]  # pixels per tick
time = 0 # time for increasing speed
ball_pos = init_pos
# define event handlers
def tick():
    global time
    time = time + 1

def draw(canvas):
    # create a list to hold ball position
    global ball_pos, time
    # calculate ball position
    ball_pos[0] = ball_pos[0] + time * vel[0]
    ball_pos[1] = ball_pos[1] + time * vel[1]
    if ball_pos[0] > WIDTH or ball_pos[0] < 0:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        time = 0
    if ball_pos[1] > HEIGHT or ball_pos[1] < 0:
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        time = 0
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
def button_handler():
    global ball_pos, time
    time = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    pass
### handles for keys    
def keydown(key):
    
    global WIDTH, HEIGHT, timer, ball_pos, vel, time
    if key == simplegui.KEY_MAP["left"]:
        timer.stop()
        vel[0] = -1
        timer.start()
    elif key == simplegui.KEY_MAP["right"]:
        timer.stop()
        vel[0] = 1
        timer.start()
    elif key == simplegui.KEY_MAP["down"]:
        timer.stop()
        vel[1] = 1
        timer.start()
    elif key == simplegui.KEY_MAP["up"]:
        timer.stop()
        vel[1] = -1
        timer.start()
    elif key == simplegui.KEY_MAP["space"]:
        if timer.is_running():
            timer.stop()
            time = 0
            vel = [0,0]
        else:
            timer.start()
        
# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)
label1 = frame.add_label('Use arrow keys to control ball', 200)
label_space = frame.add_label('')
label2 = frame.add_label('If you want stop the ball, use space key', 200)
label2_1 = frame.add_label('It also set speed to 0', 200)
label_space2 = frame.add_label('')
label3 = frame.add_label('The speed of ball is increasing rapidly', 200)
label_space3 = frame.add_label('')
label4 = frame.add_label('If you want reset the position of ball, click "Reset" button', 200)
label_space4 = frame.add_label('')
# register event handlerstick
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
timer = simplegui.create_timer(1000, tick)
button1 = frame.add_button('Reset position', button_handler)
# start frame
frame.start()
timer.start()
