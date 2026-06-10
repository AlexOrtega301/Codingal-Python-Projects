def romb(n,symbol):
    space = " "
    for i in range(n):
        print((n-i)*space,i*symbol*2)
    for i in range(n,0,-1):
        print((n-i)*space,i*symbol*2)

def tree(n,symbol):
    space = " "
    for i in range(n):
        print((n-i)*space,i*symbol*2)

romb(5, "^")
romb(6, '@')
romb(5, '?')
