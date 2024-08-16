class Demo():
    def __init__(self):
        self.a=input("Enter String")

    def __add__(self,obj):
        c=self.a+obj.a
        print("Addition=",c)


ob=Demo()
ob1=Demo()
ob+ob1
        
        
