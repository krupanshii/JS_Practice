var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)



x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)



