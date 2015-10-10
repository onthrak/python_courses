### bad way to do this but fuck it
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst.append(line)


x = lst    
y1 = x[0].split()
y2 = x[1].split()
y3 = x[2].split()
y4 = x[3].split()
z = []
### check if it strings is already in z 
for i in y1:
    if i not in z:
        z.append(i)
for i in y2:
    if i not in z:
        z.append(i)
for i in y3:
    if i not in z:
        z.append(i)
for i in y4:
    if i not in z:
        z.append(i)

#print y1, y2, y3, y4
#print
z.sort()
print z


