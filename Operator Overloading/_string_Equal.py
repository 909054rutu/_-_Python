class Demo:
    def __init__ (self):
        self.a=input("Enter String")

    def __eq__ (self,obj):
        if self.a==obj.a:
            print("String are Equal")
        else:
            print("String are Not Equal")
            
ob=Demo()
ob1=Demo()
ob==ob1
