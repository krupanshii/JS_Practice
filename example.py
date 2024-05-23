str1 = "The lion is the king of the forest."
count = 1
for char in str1:
    if char == " ":
        count += 1

print(count)

l1 = str1.split()
print(l1)
count1 = l1.__len__()
print(count1)

str2 = "thequickbrownfoxjumpoverthelazydog"
 
l = set(str2)
print(counter(l))
