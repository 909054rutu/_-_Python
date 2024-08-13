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
ob.accept(101,"sai",88.88)
ob.disp()
