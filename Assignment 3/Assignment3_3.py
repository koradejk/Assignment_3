n=int(input("Enter the length of list:"))
list=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    list.append(element)
print("The list of given number is",list)
list.sort()
min=list[0]
for i in range(0,n):
    if(list[i]<min):
        min=list[i]
print("the smallest number in the list=",min)
