n=int(input("Enter the length of list:"))
list=[]
for i in range(0,n):
    element=int(input("Enter the element:"))
    list.append(element)
print("The list of given number is:",list)

for element in list:
    if element>1:
        for i in range(2,element):
            if(element%i)==0:
                break
        else:
            print("Prime number present in given list:",element)













