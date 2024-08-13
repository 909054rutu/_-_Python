class student:
    def accept(self):
        self.rno=input("Enter Roll No")
        self.name=input("Enter Name")
        self.per=input("Enter Per")

    def disp(self):
            print("Roll No=",self.rno)
            print("Name =",self.name)
            print("Percentage=",self.per)

ob=student()
ob.accept()
ob.disp()
            
