x=8
y=10
y += x
k=2
mass_in_ounces=1
mass_in_grams=mass_in_ounces/0.035274




print "**********************"
p=0
q=0
print not (p or not q)


print "**********************"

def do_stuff():
    print "Hello world"
    print "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()
do_stuff()


print " &&&&&&&&&&&&&&"
def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()

print" BBBBBBBBBBBBBBBBBBBBB"
n=567
print (n // 10) % 10
print n % 100, n % 10
print n // 10

print " OOOOOOOOOOOOOOOOOOOO"
def mat_fun(x):
    return -5*(x**5)+(69*(x**2))-47


print mat_fun(0)
print mat_fun(1)
print mat_fun(2)
print mat_fun(3)

print "##############" 

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    FV=present_value*(1+rate_per_period)**periods
    # Put your code here.
    return FV

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print future_value(2500, .03, 12, 5)
print future_value(500, .04, 10, 10)


print " @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ "

import math ### needed to calculate tan

def polygon(n,s):
    area=((1.0/4.0)*n*(s**2))/math.tan(math.pi/n)
    return area

print polygon(5,7) ## test
print polygon(7,3) ## answer


print " 88888888888888888888888" 
def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c)) ### now its good
print max_of_3(2,6,7)

print "565656565656565656656565656"

import math
def project_to_distance(point_x,point_y,distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)





