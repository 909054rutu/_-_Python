

class string:
    def get_s(self):
        self.s=input("enter string")
    def disp(self):
        print(self.s.upper())
        word=self.s
        print(word[::-1])
ob=string()
ob.get_s()
ob.disp()
