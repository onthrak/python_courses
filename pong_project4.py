# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 15
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
init_pos = [WIDTH / 2, HEIGHT / 2]
ball_pos = init_pos ### initial position of ball - middle of area
score1 = 0
score2 = 0
ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = [[PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT ],[PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]] ## has to be changed 
paddle2_pos = [[WIDTH - PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT ],[WIDTH - PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]## has to be changed


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = init_pos[0]
    ball_pos[1] = init_pos[1]
    ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]

    if direction == LEFT:
        ball_vel[0] = ball_vel[0] * (-1)
        ball_vel[1] = ball_vel[1] 
    if  direction == RIGHT:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = ball_vel[1] 



# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, init_pos    # these are numbers
    global score1, score2  # these are ints
    global LEFT, RIGHT
    global WIDTH, HEIGHT
    score1 = 0
    score2 = 0
    acc = 0
    ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]
    ball_pos[0] = 300
    ball_pos[1] = 200
    if LEFT:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, init_pos, LEFT, RIGHT
 
    ## colision on canvas   
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] - BALL_RADIUS < 0 or ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]
    ## player 1
    elif ball_pos[0] - BALL_RADIUS < paddle1_pos[1][0] and not paddle1_pos[0][1] - BALL_RADIUS < ball_pos[1]  < paddle1_pos[1][1] + BALL_RADIUS:
        ball_pos[0] = 300
        ball_pos[1] = 200
        LEFT = False
        RIGHT = True
        score2 += 1 ## for player 2
        if LEFT:
            spawn_ball(LEFT)
        else:
            spawn_ball(RIGHT)
        

    ## player 2 
    elif ball_pos[0] - BALL_RADIUS > paddle2_pos[1][0] and not paddle2_pos[0][1] - BALL_RADIUS < ball_pos[1]  < paddle2_pos[1][1] + BALL_RADIUS:
        ball_pos[0] = 300
        ball_pos[1] = 200
        LEFT = True
        RIGHT = False
        score1 += 1 ## for player 1
        if LEFT:
            spawn_ball(LEFT)
        else:
            spawn_ball(RIGHT)
        
    else:
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    # update paddle's vertical position, keep paddle on the screen
    ## paddle 1 
    paddle1_pos[0][1] = paddle1_pos[0][1] + paddle1_vel
    paddle1_pos[1][1] = paddle1_pos[1][1] + paddle1_vel
    if paddle1_pos[0][1] < 0:
        paddle1_pos[0][1] = 0
        paddle1_pos[1][1] = PAD_HEIGHT
    if paddle1_pos[1][1] > HEIGHT:
        paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle1_pos[1][1] = HEIGHT
    ## paddle 2 
    paddle2_pos[0][1] = paddle2_pos[0][1] + paddle2_vel
    paddle2_pos[1][1] = paddle2_pos[1][1] + paddle2_vel
    if paddle2_pos[0][1] < 0:
        paddle2_pos[0][1] = 0
        paddle2_pos[1][1] = PAD_HEIGHT
    if paddle2_pos[1][1] > HEIGHT:
        paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
        paddle2_pos[1][1] = HEIGHT

    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], 5, "Red") ### 1st left paddle
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], 5, "Green")  ### 2nd right paddle
    # determine whether paddle and ball collide
    ## 1st paddle
    if paddle1_pos[1][0] + BALL_RADIUS >= ball_pos[0] and (paddle1_pos[0][1] - BALL_RADIUS <= ball_pos[1]  <= paddle1_pos[1][1] + BALL_RADIUS):
        ball_vel[0] = ball_vel[0] * 1.1 ## increse the velocity by 10% when hit 
        ball_vel[1] = ball_vel[1] * 1.1 ## increse the velocity by 10% when hit
        ball_vel[0] = -ball_vel[0]

    ## 2nd paddle
    if paddle2_pos[1][0] - BALL_RADIUS <= ball_pos[0] and (paddle2_pos[0][1] - BALL_RADIUS <= ball_pos[1]  <= paddle2_pos[1][1] + BALL_RADIUS):
        ball_vel[0] = ball_vel[0] * 1.1 ## increse the velocity by 10% when hit
        ball_vel[1] = ball_vel[1] * 1.1 ## increse the velocity by 10% when hit
        ball_vel[0] = -ball_vel[0]

    

    # draw score
    canvas.draw_text(str(score1), (80, 40), 48, 'Red') ## for player 1
    canvas.draw_text(str(score2), (WIDTH - 80, 40), 48, 'Green') ## for player 2   

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos,  paddle2_pos, acc
    acc = 2 
    if key == simplegui.KEY_MAP["w"]:
        if paddle1_pos[0][1] - HALF_PAD_HEIGHT < 0:
            acc = 0
        else:
            paddle1_vel -= acc

    if key == simplegui.KEY_MAP["up"]:
        if paddle2_pos[0][1] - HALF_PAD_HEIGHT < 0:
            acc = 0
        else:
            paddle2_vel -= acc

    if key == simplegui.KEY_MAP["s"]:
        if paddle1_pos[1][1] + HALF_PAD_HEIGHT > HEIGHT:
            acc = 0
        else:
            paddle1_vel += acc

    if key == simplegui.KEY_MAP["down"]:
        if paddle2_pos[1][1] + HALF_PAD_HEIGHT > HEIGHT:
            acc = 0
        else:
            paddle2_vel += acc
    

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_pos[0][1] = paddle1_pos[0][1] - paddle1_vel
        paddle1_pos[1][1] = paddle1_pos[1][1] - paddle1_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_pos[0][1] = paddle2_pos[0][1] - paddle2_vel
        paddle2_pos[1][1] = paddle2_pos[1][1] - paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_pos[0][1] = paddle1_pos[0][1] + paddle1_vel
        paddle1_pos[1][1] = paddle1_pos[1][1] + paddle1_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_pos[0][1] = paddle2_pos[0][1] + paddle2_vel
        paddle2_pos[1][1] = paddle2_pos[1][1] + paddle2_vel

### button handler for reseting game
def button_handler():
    global new_game
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset game', button_handler)
labelspace1 = frame.add_label('')
label1 = frame.add_label('Red player: Keys: W and S')
labelspace2 = frame.add_label('')
label2 = frame.add_label('Green player: Keys: Up and Down')
labelspace3 = frame.add_label('')
label3 = frame.add_label('If you want reset game, click reset button')


# start frame
new_game()
frame.start()
