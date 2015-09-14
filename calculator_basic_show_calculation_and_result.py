# calculator with all buttons


import simplegui


# intialize globals
""" for example:
you want get result from 2**10
so store is 2 and operand is 10
then you click button "exp"
and you click button "Show result"
and you get result in window
"""

x=float(raw_input("set store")) ## 
y=float(raw_input("set operand")) ##
store = x
operand = y
message = str(round(store,4))
# new line
oper_msq = str(0)
# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""
    
    
def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    #new line
    global oper_msq
    oper_msq="swapped"
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    global oper_msq
    oper_msq=str(round(store-operand,4))+" + "+str(round(operand,4))
    global message
    message = str(round(store,4))
    output()
    
def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    global oper_msq
    oper_msq=str(round(store+operand,4))+" - "+str(round(operand,4))
    global message
    message = str(round(store,4))
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    global oper_msq
    oper_msq=str(round(store/operand,4))+" * "+str(round(operand,4))
    global message
    message = str(round(store,4))
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    global oper_msq
    oper_msq=str(round(store*operand,4))+" / "+str(round(operand,4))
    global message
    message = str(round(store,4))
    output()
    
def exp():
    """ exponate store by operand """
    global store
    store = store ** operand
    global oper_msq
    oper_msq=str(round(store**(1/operand),4))+" ^ "+str(round(operand,4))
    global message
    message = str(round(store,4))
    output()
    
def root():
    """ root store by operand """
    global store
    store= store ** (1.0/operand)
    global oper_msq
    oper_msq=str(round(store**operand,4))+" ^(1/"+str(round(operand,4))+ ")"
    global message
    message = str(round(store,4))
    output()
    
def new_var():
    """ sets new store and operand """
    x=float(raw_input("set store")) ##
    y=float(raw_input("set operand")) ##
    global store
    store= x
    global operand
    operand = y
    global message
    message = str(round(store,4))
    output()
    global oper_msq
    oper_msq=str(0)  
    
def enter(t):
    """ enter a new operand"""
    global operand
    operand = float(t)
    output()    

# Handler for mouse click
def click():
    global message
    message = str(round(store,4))
    global oper_msq
    oper_msq = oper_msq
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text('RESULT:', [50, 50], 48, 'Blue', "sans-serif")
    canvas.draw_text(message, [50,150], 64, "Green")
    canvas.draw_text(oper_msq, [50,250], 48, "red")

# create frame
f = simplegui.create_frame("Calculator",700,300)
#f.add_button("Show result", click, 200)
f.set_draw_handler(draw)
    
# register event handlers
#f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_button("Exp", exp, 100)
f.add_button("Root",root,100)
f.add_button("NEW VARIABLES", new_var, 200)
f.add_input("Enter new operand", enter, 100)

# get frame rolling
f.start()