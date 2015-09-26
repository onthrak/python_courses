### program for end of programming course
### "Programming for Everybody (Getting Started with Python)"
alist = []
def prog():
    global alist
    while True:
        givint = raw_input("Enter a number: ")
        if givint == 'done':
            break
        else:
            try:
                lic = int(givint)
                alist.append(lic)
                
            except:
                print "Invalid input"

prog()
### numbers : 4 ,5 , bad data, 7 , done
print 'Maximum is '+str(max(alist))
print 'Minimum is '+str(min(alist))