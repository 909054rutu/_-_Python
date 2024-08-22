class Circle:
    def accept(Self):
        Self.r=float(input("Enter Radius"))


class Area(Circle):
    def cal(Self):
        a=3.14*Self.r*Self.r
        print("Area Of Circle:",a)


ob=Area()
ob.accept()
ob.cal()
        
