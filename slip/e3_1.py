#A) Write a Python program to check if a given key already exists in a dictionary. If
#key exists replace with another key/value pair.

d={"name":"rutuja","per":99,"age":19}
key=input("enter key")
if key in d:
    val=input("enter value")
    d[key]=val
    print(d)
