class Student:
    def accept(self,rno,name,per):
        self.rno=rno;
        self.name=name;
        self.per=per;

    def disp(self):
        print("Roll no:",self.rno)
        print("Name:",self.name)
        print("Per:",self.per)

ob=Student()
rno=input("Enter Roll no")
name=input("Enter Name")
per=input("Enter Per")
ob.accept(rno,name,per)
ob.disp()
