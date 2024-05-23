l1 = [ 10,20,30,40,50 ]
l2 = [ 10,20,30,50,10,20,110 ]

s1 = set(l1)
s2 = set(l2)

s = s1-s2
t = s2-s1

print(s.union(t))