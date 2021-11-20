mylist = [3,5,7,9,10.5]
print(mylist)
mylist.append("Python")
print(len(mylist))
print('-----------------')
print (mylist[0])
print(mylist[len(mylist)-1])
for count in mylist[2:5]:
    print(count)

mylist.remove("Python")