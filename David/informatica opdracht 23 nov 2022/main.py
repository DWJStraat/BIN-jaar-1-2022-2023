def aaa(a,b):
    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))
    print('-' * 20)


a = {12, 5, 17, 6}
b = {42, 17, 6}
c = {21, 76, 10, 3, 9}
d = {}
e = {87}
f = {22, 87, 23}

aaa(a,b)
aaa(c,d)
aaa(e,f)



