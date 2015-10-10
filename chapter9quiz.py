counts = {'aa':45, 'bb':[67,45,76]}
key = 'aa'
if key in counts:
    counts[key] = counts.get(key,0) + 2
else:
    counts[key] = 1
    
print counts.values()
x = counts.values()
for i in x:
    try:
        for ii in i:
                print ii
    except:
        print i
