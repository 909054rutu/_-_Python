
class emp:
    def accept(self):
        self.id=input("enter id")
        self.sal=int(input("enter sal"))

class mang(emp):
    def bonus(self):
        self.bonus=int(input("Enter bonus"))
        self.tot=self.sal+self.bonus

    def disp(self):
        print("Id",self.id)
        print("sal",self.sal)
        print("tot",self.tot)

a=[]
n=int(input("Enter limit"))
for i in range(0,n):
    ob=mang()
    ob.accept()
    ob.bonus()
    a.append(ob)
maxx=a[0].tot
index=0
for i in range(1,n):
    if maxx<a[i].tot:
        maxx=a[i].tot
        index=i

a[index].disp()
