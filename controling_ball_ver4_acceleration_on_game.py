# Ball motion with a defined timer
# Speed of ball is increasing for every 1 second
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
# Initialize globals
WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 20
OBS_RADIUS = 25
last_score = 0
best_score = [0]
init_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0,0]  # pixels per tick
time = 0 # time for increasing speed
ball_pos = init_pos
### initial score player
score = 0 ### it will increasing per second

### obstacles 
obs1_pos = [random.randint(100, init_pos[0] - 150),random.randint(100, init_pos[1] - 150)]
obs2_pos = [random.randint(100, init_pos[0] - 150),random.randint(100, init_pos[1] + 150)]
obs3_pos = [random.randint(100, init_pos[0] + 150),random.randint(100, init_pos[1] - 150)]
obs4_pos = [random.randint(100, init_pos[0] + 150),random.randint(100, init_pos[1] + 150)]
obs5_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
obs6_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
obs7_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
obs8_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
obs9_pos = [random.randint(100, 200),random.randint(init_pos[1] + 200, HEIGHT - 50)] ### lower right
obs10_pos = [random.randint(init_pos[0] + 200, WIDTH - 50),random.randint(100, 200)] ### upper left
# define event handlers
def tick():
    global time, score
    time = time + 1
    score = score + 1 + score ** (1/2.0)
# when you touch obstacles or go behind canvas
def you_lose():
    global ball_pos, time, score, timer, vel, init_pos
    global WIDTH, HEIGHT, last_score, best_score
    global obs1_pos, obs2_pos, obs3_pos, obs4_pos, obs5_pos 
    global obs6_pos, obs7_pos, obs8_pos, obs9_pos, obs10_pos
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    time = 0
    last_score = score ### add last score
    best_score.append(last_score) ### add scores to list
    score = 0
    vel = [0,0]
    init_pos = [WIDTH / 2, HEIGHT / 2]
    timer.stop()
    obs1_pos = [random.randint(100, init_pos[0] - 150),random.randint(100, init_pos[1] - 150)]
    obs2_pos = [random.randint(100, init_pos[0] - 150),random.randint(100, init_pos[1] + 150)]
    obs3_pos = [random.randint(100, init_pos[0] + 150),random.randint(100, init_pos[1] - 150)]
    obs4_pos = [random.randint(100, init_pos[0] + 150),random.randint(100, init_pos[1] + 150)]
    obs5_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
    obs6_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
    obs7_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
    obs8_pos = [random.randint(init_pos[0] + 100, WIDTH - 150),random.randint(init_pos[1], HEIGHT - 150)]
    obs9_pos = [random.randint(100, 200),random.randint(init_pos[1] + 200, HEIGHT - 50)] ### lower right
    obs10_pos = [random.randint(init_pos[0] + 200, WIDTH - 50),random.randint(100, 200)] ### upper left   
def draw(canvas):
    # create a list to hold ball position
    global ball_pos, time, score, WIDTH, HEIGHT 
    # calculate ball position
    ball_pos[0] = ball_pos[0] + time * vel[0]
    ball_pos[1] = ball_pos[1] + time * vel[1]
    if ball_pos[0] > WIDTH or ball_pos[0] < 0:
        you_lose()
    if ball_pos[1] > HEIGHT or ball_pos[1] < 0:
        you_lose()
    #### test if ball touch obstacle, good :D
    ## 1st obstacle
    if obs1_pos[0] - 37 <= ball_pos[0] <= obs1_pos[0] + 37 and \
       obs1_pos[1] - 37 <= ball_pos[1] <= obs1_pos[1] + 37 :
        you_lose()
    ## 2nd obstacle    
    if obs2_pos[0] - 37 <= ball_pos[0] <= obs2_pos[0] + 37 and \
       obs2_pos[1] - 37 <= ball_pos[1] <= obs2_pos[1] + 37 :
        you_lose()
    ## 3rd obstacle
    if obs3_pos[0] - 37 <= ball_pos[0] <= obs3_pos[0] + 37 and \
       obs3_pos[1] - 37 <= ball_pos[1] <= obs3_pos[1] + 37 :
        you_lose()
    ## 4th obstacle
    if obs4_pos[0] - 37 <= ball_pos[0] <= obs4_pos[0] + 37 and \
       obs4_pos[1] - 37 <= ball_pos[1] <= obs4_pos[1] + 37 :
        you_lose()
    ## 5th obstacle
    if obs5_pos[0] - 37 <= ball_pos[0] <= obs5_pos[0] + 37 and \
       obs5_pos[1] - 37 <= ball_pos[1] <= obs5_pos[1] + 37 :
        you_lose()
    ## 6th obstacle
    if obs6_pos[0] - 37 <= ball_pos[0] <= obs6_pos[0] + 37 and \
       obs6_pos[1] - 37 <= ball_pos[1] <= obs6_pos[1] + 37 :
        you_lose()
    ## 7th obstacle
    if obs7_pos[0] - 37 <= ball_pos[0] <= obs7_pos[0] + 37 and \
       obs7_pos[1] - 37 <= ball_pos[1] <= obs7_pos[1] + 37 :
        you_lose()
    ## 8th obstacle
    if obs8_pos[0] - 37 <= ball_pos[0] <= obs8_pos[0] + 37 and \
       obs8_pos[1] - 37 <= ball_pos[1] <= obs8_pos[1] + 37 :
        you_lose()
    ## 9th obstacle
    if obs9_pos[0] - 37 <= ball_pos[0] <= obs9_pos[0] + 37 and \
       obs9_pos[1] - 37 <= ball_pos[1] <= obs9_pos[1] + 37 :
        you_lose()
    ## 10th obstacle
    if obs10_pos[0] - 37 <= ball_pos[0] <= obs10_pos[0] + 37 and \
       obs10_pos[1] - 37 <= ball_pos[1] <= obs10_pos[1] + 37 :
        you_lose()
    ### draw a score of player
    canvas.draw_text('score: '+str(int(score)), (WIDTH - 250, 50), 64, 'Red')
    canvas.draw_text('last score: '+str(int(last_score)), (50, 50), 28, 'Green')
    canvas.draw_text('best score: '+str(int(max(best_score))), (50, 80), 28, 'White')
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    # draw obstacles
    canvas.draw_circle(obs1_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs2_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs3_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs4_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs5_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs6_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs7_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs8_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs9_pos, OBS_RADIUS, 9, "Orange", "Grey")
    canvas.draw_circle(obs10_pos, OBS_RADIUS, 9, "Orange", "Grey")
def button_handler():
    global ball_pos, time, timer
    time = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel = [0,0]
    timer.stop()
    pass
### handles for keys    
def keydown(key):
    
    global WIDTH, HEIGHT, timer, ball_pos, vel, time,score
    if key == simplegui.KEY_MAP["left"]:
        vel[0] = -1
        timer.start()
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] = 1
        timer.start()
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] = 1
        timer.start()
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] = -1
        timer.start()
    elif key == simplegui.KEY_MAP["space"]:
        if timer.is_running():
            timer.stop()
            time = 0
            vel = [0,0]
            score = score / 2.0
        else:
            timer.start()
        
# create frame
frame = simplegui.create_frame("Ball game", WIDTH, HEIGHT)
label1 = frame.add_label('Use arrow keys to control ball', 200)
label_space = frame.add_label('')
label2 = frame.add_label('If you want stop the ball, use space key', 200)
label2_1 = frame.add_label('It also set speed to 0', 200)
label2_2 = frame.add_label('But when you stop, your score is decreased by half!', 200)
label_space2 = frame.add_label('')
label3 = frame.add_label('The speed of ball is increasing rapidly', 200)
label_space3 = frame.add_label('')
label4 = frame.add_label('If you want reset the position of ball, click "Reset" button', 200)
label_space4 = frame.add_label('')
label5 = frame.add_label('Of course you have to dodge the obstacles', 200)
label_space5 = frame.add_label('')
label6 = frame.add_label('If you touch them, you lose', 200)
label_space6 = frame.add_label('')
label_space7 = frame.add_label('')
# register event handlerstick
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
timer = simplegui.create_timer(1000, tick)
button1 = frame.add_button('Reset position', button_handler)
# start frame
frame.start()

