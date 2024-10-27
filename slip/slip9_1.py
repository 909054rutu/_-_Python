class string:
    def get(self):
        self.s=input("Enter string")

    def prints(self):
        s1=self.s
        print(s1[::-1])

ob=string()
ob.get()
ob.prints()
