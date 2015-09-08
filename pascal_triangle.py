# Prints Pascal's triangle
# Enter the number of rows you want in A1; prints 10 by default

def pascal(n):
    Cell(1,n+2).value = 1
    for row in xrange(2,n+2):
        for i in xrange(row):
            col = (n+2-row) + 2*i + 1
            left = Cell(row, col).offset(-1, -1).name
            right = Cell(row, col).offset(-1, 1).name
            Cell(row, col).formula = '=%s + %s' %(left, right)

rows = Cell("A1").value
if (type(rows)!= int) or (rows < 1):
    rows = 10
pascal(rows)
