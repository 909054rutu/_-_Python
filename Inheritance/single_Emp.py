class Emp:
    def accept(Self):
        Self.eno=input("Enter No")
        Self.ename=input("Enter Name")
        Self.Sal=input("Enter Sal")


class info(Emp):
    def disp(Self):
       print("Emp no=", Self.eno)
       print("Emp Name=",Self.ename)
       print("Emp Sal=", Self.Sal)


ob=info()
ob.accept()
ob.disp()
        
