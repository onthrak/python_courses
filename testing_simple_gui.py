import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

message = "Welcome!"

# Handler for button click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)

frame.set_canvas_background('#00FFFF')
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()