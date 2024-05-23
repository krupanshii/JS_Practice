List = [3,1,2,3,0,8,2,0,0,3]

List[-1]
print(List[-1])

if int(List[-1]) % 2 == 0:
    print("Even number")
    List.append(0)
    print(List)
else:
    print("Odd number")
    List.append(1)
    print(List)

if 0 in List:
    for i in range(len(List)):
        List.remove(0)
        List.append(0)
print(List)

List2 = [0,1,3,1,9]

if 0 in List2:
    for i in range(len(List2)):
        List2.remove(0)
        List2.append(0)
print(List2)


for x in List:
    count = List.count(x)
    if count == 1:
        print(x)










