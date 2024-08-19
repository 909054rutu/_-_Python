class Demo:
    def accept(self):
         self.s1=input("Enter string")
         self.n=int(input("Enter number"))

    def __mul__(self,obj):
     
        print(self.s1*self.n)


ob=Demo()
ob1=Demo()
ob.accept()
ob*ob1
    
