n=int(input("Enter the length of list:"))
list=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    list.append(element)
print("The list of given number is",list)
no=int(input("enter the number to find frequency:"))
def count(list,no):
    count=0
    for element in list:
        if(element==no):
            count=count+1
    return count
print("Frequency of given number in list:",count(list,no))