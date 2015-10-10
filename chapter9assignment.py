name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
x = list()
for line in handle:
    line.split() ## unnesssecary
    if line.startswith("From "):
        x.append(line[line.find(" ")+1:line.find(" ",line.find(" ")+1)])



counts = dict()
for name in x:  
  if name not in counts:  
    counts[name]=1  
  else:  
    counts[name] = counts[name] + 1  
    

### print max of numbers mails and name with max numbers of mails

for names,vals in counts.items():
    if vals == max(counts.values()):
    	print names,vals

    
    