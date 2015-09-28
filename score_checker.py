x = raw_input("give a score: ")
if float(x) >= 0.0 and float(x) <= 1.0:
    if float(x) < 0.6:
        print 'F'
    elif float(x) >= 0.6 and float(x) < 0.7:
        print 'D'
    elif float(x) >= 0.7 and float(x) < 0.8:
        print 'C'
    elif float(x) >= 0.8 and float(x) < 0.9:
        print 'B'
    elif float(x) >= 0.9 and float(x):
        print 'A'
else:
    print 'value out of range'