class Emp:
    def __init__(self):
        self.eno=input("Enter Emp No")
        self.ename=input("Enter Emp Name")
        self.sal=input("Enter Sal")

    def disp(self):
        print("Emp No=",self.eno)
        print("Emp Name=",self.ename)
        print("Emp sal=",self.sal)


ob=Emp()
ob.disp()
