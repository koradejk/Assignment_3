n=int(input("Enter the length of list:"))
list=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    list.append(element)
print("The list of given number is",list)
total=0
for element in range(0,len(list)):
    total=total+list[element]
print("The sum of all the element given in list:",total)