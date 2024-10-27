#A) Write a Python program to accept n numbers in list and remove duplicates from a
#list. [15 M]

l=[]
n=int(input("enter limit"))
for i in range(0,n):
    num=int(input("enter number"))
    l.append(num)
    print(l)
b=set(l)
print(b)
