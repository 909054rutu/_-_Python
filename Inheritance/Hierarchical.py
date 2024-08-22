class Area:
    def acceptS(Self):
        Self.s=int(input("Enter Side"))
    def acceptR(Self):
        Self.base=float(input("Enter Base"))
        Self.Height=float(input("Enter Height"))

class Square(Area):
    def cal(Self):
        square=Self.s*Self.s
        print("Square:",square)
    
class Triangle(Area):
    def cal(Self):
        Triangle=Self.base*Self.Height
        print("Area of Triangle:",Triangle)


ob=Square()
ob.acceptS()
ob.cal()
ob1=Triangle()
ob1.acceptR()
ob1.cal()

