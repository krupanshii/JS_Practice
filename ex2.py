# # '''
# # numbers = [1, 2, 1, 3, 4, 2 , 2,2,2]
# # count = numbers.count(3)
# # print(count)


# # strOne = str("pynative")
# # strTwo = "pynative"
# # print(strOne == strTwo)
# # print(strOne is strTwo)

# # str1 = 'Welcome'
# # print(str1*2)

# # str1 = "My salary is 7000";
# # str2 = "7000"

# # print(str1.isdigit())
# # print(str2.isdigit())

# # str1 = "my isname isisis jameis isis bond";
# # sub = "is";
# # print(str1.count(sub, 4))

# # str1 = "PYnative"
# # print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])

# # print("John" > "Jhon")
# # print("Emma" < "Emm")

# # str = "my name is James bond";
# # print (str.capitalize())

# # myString = "pynative"
# # stringList = ["abc", "pynative", "xyz"]

# # print(stringList[1] == myString)
# # print(stringList[1] is myString)

# # str = "My salary is 7000";
# # print(str.isalnum())

# # str1 = "My salary is 7000";
# # str2 = "7000"

# # # print(str1.isdigit())
# # # print(str2.isdigit())
# # # '''

# # # var= "James Bond"
# # # print(var[2::-1])


# def fun1(name, age):
#     print(name, age)

# fun1("Emma", age=23)
# fun1(age =23, name="Emma")
# # fun1(name="Emma", 23)
# # fun1(age =23, "Emma")

# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)

# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d

#     return inner_fun(a, b)
#     return a

# result = outer_fun(5, 10)
# print(result)

# def fun1(num):
#     return num + 25

# fun1(5)
# print(num)


# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# # display(emp="Kelly", salary=9000)

# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)

# res = outer_fun(5, 10)
# print(res)

def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")