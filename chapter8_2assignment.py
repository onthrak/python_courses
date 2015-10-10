### for txt file :  "mbox-short.txt"
fname = ''
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
xlist = list()
for line in fh:
    if line.startswith('From '):
    	xf = line.split()
    	xlist.append(xf[1])
    	count += 1
for line in xlist:
	print line    	
print "There were", count, "lines in the file with From as the first word"
