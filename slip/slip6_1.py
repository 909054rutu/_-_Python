class complex():
    def base_complex(self):
        self.real_part=input("enter real part")
        self.img_part=input("enter img part")

    def disp(self):
        print("img part real part",self.real_part,"+",self.img_part,"i",sep="")

    def sum(self,c1,c2):
        self.real_part=c1.real_part+c2.real_part
        self.img_part=c1.img_part+c2.img_part

c1=complex()
c2=complex()
c3=complex()

print("enter first complex number")
c1.base_complex()
print("first complex number",end=" ")
c1.disp()

print("sec complex number",end=" ")
c2.base_complex()
print("scecond complex number",end=" ")
c2.disp()

c3.sum(c1,c2)
print("sum",end=" ")
c3.disp()

