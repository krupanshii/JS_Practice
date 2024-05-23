
#  X=300 
#  Y= 17
#  X%=Y
#  print(X)

#  a = 3
#  b = "12"

#  print(a*b)

#  a = -9//7
#  print(a)

#  x=15
#  y = str(float(x))

#  print(type(y))

#  x = "Mayur"

#  float(x)

# #  x = 10
# #  y =5
# #  z=3

#  ans = x + y % z

#  print(ans)

#  j=6
#  g=3.3

#  print(type(j/g))
#  print(type(j//g))

#  a=5
# b=3

#  print(a&b)

# # # # # Product = ['Pencil', 'Pen', 'Eraser', 'Pencil Box', 'Scale']
# # # # # Price= [5, 10, 2, 20, 12]  
# # # # # Brand = ['Camlin', 'Rotomac', 'Nataraj', 'Camel', 'Apsara']
# # # # # Stationery = [Product, Price, Brand]

# # # # # Stationery[0].append('Notebook')
# # # # # print(Stationery)

# # # # # Stationery[0].insert(0,'Notebook')
# # # # # print(Stationery)

# # # # # Stationery[0][1] = "Notebook"
# # # # # print(Stationery)

# # # # # Stationery[0].extend('Notebook')
# # # # # print(Stationery)

# # # # # Mylist =['a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e'] 

# # # # # print(Mylist.index('d'))

# # # # s = {1,2,4,5}
# # # # l=[]

# # # # for i in range(len(s)):
# # # #     l +=[1+i]

# # # # print(l)

# # # import numpy as np

# # # arr = np.array(np.arange(0,15))
# # # print(arr.reshape(3,5))

# # t1=(1,2,"tuple",4)
# # t2=(5,6,7)

# # #t1.append(5)

# # x=t2[t1[1]]
# # print(x)

# # t4=t1+t2
# # print(t4)

# # t5=(t1,t2)
# # print(t5)

# # t6=(list(t1), list(t2))
# # print(t6)

# def g(y):
#     b = 0
#     while y >= 3:
#         (y,b) = (y/3,b+1)
#     return(b)

# print(g(728))

# def f(n):
#     s = 0
#     for i in range(2,n):
#         if n%i == 0 and i%2 == 1:
#             s = s+1
#     return(s)

# print(f(90)-f(89))

# def h(n):
#     s = True
#     for i in range(1,n+1):
#         if i*i == n:
#             s = False
#     return(s)

# print(h(3))
# print(h(2))
# print(h(49))
# print(h(6))

# def foo(m):
#     if m == 0:
#       return(0)
#     else:
#       return(m+foo(m-1))
    
# print(foo(1))

# x = ["slithy",[7,10,12],2,"tove",1]  # Statement 1
# y = x[0:50]                          # Statement 2
# z = y                                # Statement 3
# w = x                                # Statement 4
# x[0] = x[0][:5] + 'ery'              # Statement 5
# y[2] = 4                             # Statement 6
# z[4] = 42                            # Statement 7
# w[0][:3] = 'fea'                     # Statement 8
# x[1][0] = 5555                       # Statement 9
# a = (x[4][1] == 1)    

# b = [23,44,87,100]
# a = b[1:]
# d = b[2:]
# c = b
# d[0] = 97
# c[2] = 77

# print(a,b,c,d)

# startmsg = "python"
# endmsg = ""
# for i in range(1,1+len(startmsg)):
#   endmsg = startmsg[-i] + endmsg

# print(endmsg)

def mystery(l):
  l = l[1:]
  return()

mylist = [7,11,13]
print(mystery(mylist))