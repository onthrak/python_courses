name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
###
### finding lines start with "From "

x = list()
for line in handle:
    line.split() 
    #### adding to list only hours
    if line.startswith("From "):
        x.append(line[line.find(":")-2:line.find(":")])
		

x.sort()       


counts = dict()
for name in x:  
  if name not in counts:  
    counts[name]=1  
  else:  
    counts[name] = counts[name] + 1  
    
lost = list()    
#print counts
for key,val in counts.items():
    lost.append((key , val ))

    
lost.sort() ### list with tuples   
for items in lost:
    print items[0], items[1]

 


    
    