class string:
    def get_String(self):
        self.s=input("Enter String")

    def print_String(self):
        print(self.s.upper())
        w=self.s
        print(w[ :: -1])

ob=string()
ob.get_String()
ob.print_String()
    
