# calculator with all buttons


import simpleguitk


# intialize globals
x=float(raw_input("set store")) ##
y=float(raw_input("set operand")) ##
store = x
operand = y


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
    output()
    
def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()
def exp():
    """ exponate store by operand """
    global store
    store = store ** operand
    output()
def root():
    """ root store by operand """
    global store
    store= store ** (1.0/operand)
    output()
def new_var():
    """ sets new store and operand """
    x=float(raw_input("set store")) ##
    y=float(raw_input("set operand")) ##
    global store
    store= x
    global operand
    operand = y
    output()
# create frame
f = simpleguitk.create_frame("Calculator",300,300)

# register event handlers
f.add_button("Print", output, 100)
f.add_button("Swap", swap, 100)
f.add_button("Add", add, 100)
f.add_button("Sub", sub, 100)
f.add_button("Mult", mult, 100)
f.add_button("Div", div, 100)
f.add_button("Exp", exp, 100)
f.add_button("Root",root,100)
f.add_button("NEW VARIABLES", new_var, 200)

# get frame rolling
f.start()
