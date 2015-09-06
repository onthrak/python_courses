############
# This is a compilation of the examples from Week 1's Programming Tips.
# Many of these functions have errors, so this file won't run as is.
############


import math
print math.pi

############
# Has multiple NameErrors
def volume_cube(side):
    return side ** 3

s = 2
print "Volume of cube with side", s, "is", volume_cube(s), "."

print "+++++++++"

############
# Has a NameError
import random
def random_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1 , die2

print "Sum of two random dice, rolled once:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()

print "+++++++++"

# Has an AttributeError
def volume_sphere(radius):
    return 4.0/3.0 * math.pi * (radius ** 3)

r = 2
print "Volume of sphere of radius", r, "is", volume_sphere(r), "."

print "+++++++++"

############
# Has multiple TypeErrors
def area_triangle(base, height):
    return 0.5 * base * height

b = 5
h = 2 + 2
print "Area of triangle with base", b, "and height", h, "is", area_triangle(b,h), "."



print"UUUUUUUUUUUUUUUU"
############
# Poor readability
def area(a,b,c):
    s = (a+b+c)/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

