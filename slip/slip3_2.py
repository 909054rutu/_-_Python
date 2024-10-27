class student:
    def accept(self):
        self.rno=input("Enter rno")
        self.name=input("Enter Name")
class marks(student):
        def accept_marks(self):
            self.m1=input("enter 1 sub")
            self.m2=input("enter 2 sub")
            self.m3=input("enter 3 sub")
        def disp(self):
            print("rno",self.rno)
            print("name",self.name)
            print(self.m1+self.m2+self.m3)

ob=marks()
ob.accept()
ob.accept_marks()
ob.disp()
           

           
            
