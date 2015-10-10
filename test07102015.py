import	operator
c = {'aa':255, 'bb': 25,  'cc': 125, 'dd':255, "ee":500}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))

print tmp
tmp.sort(reverse = True)
tmp1 = sorted(tmp, key = operator.itemgetter(0, 1), reverse = True) ### find max value 
print tmp
print tmp1	

print sorted( [ (v,k) for k,v in c.items()], reverse = True)[:3] ### same results as 10 fucking lines of code, and top 3