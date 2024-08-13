class Rectangle:
    def accept(self):
        self.l=float(input("Enter Length"));
        self.w=float(input("Enter Width"));
        self.h=float(input("Enter Height"));

    def calculate(self):
        Area=self.l*self.w
        Volume=self.l*self.w*self.h
        print("Area Of Rectangle=",Area)
        print("Volume Of Rectangle=",Volume)

ob=Rectangle()
ob.accept()
ob.calculate()
    
