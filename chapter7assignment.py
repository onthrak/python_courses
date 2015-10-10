# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
x=[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        x.append(float(line[line.find('0'):])) ### take to x all numbers from txt
    

lenx = len(x)
aver_spam = sum(x) / lenx
print "Average spam confidence: "+str(aver_spam)