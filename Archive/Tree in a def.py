def tree(n,symbol):
    space = " "
    for i in range(n):
        print((n-i)*space,i*symbol*2)
tree(12,'^')
tree(6,'@')
tree(10,'?')
