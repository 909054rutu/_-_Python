n=input("Enter Number")
ecnt=zcnt=ocnt=0
for num in n:
    div=int(num)
    if div==0:
        zcnt+=1
    elif div%2==0:
        ecnt+=1
    else:
        ocnt+=1     
print("Even count=",ecnt)
print("Odd count=",ocnt)
print("Zero count=",zcnt)
