n=int(input("Enter the length of list:"))
list=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    list.append(element)
print("The list of given number is",list)
list.sort()
print("The largest element of list is",list[n-1])
