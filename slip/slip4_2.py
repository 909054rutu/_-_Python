class emp:
    def accept_e(self):
        self.idd=input("Enter idd")
        self.name=input("Enter name")
        self.sal=int(input("Enter sal"))  
class mang(emp):
    def accept_m(self):
        self.bonus=int(input("enter bonus"))
        self.tot=self.sal+self.bonus
    def disp(self):
        print("idd",self.idd)
        print("name",self.name)
        print("sal",self.tot)


n=int(input("Enter limit"))
a=[]
for i in range(0,n):
    ob=mang()
    ob.accept_e()
    ob.accept_m()
    a.append(ob)
    
max=a[0].tot
index=0
for i in range(1,n):
    if max<a[i].tot:
        max=a[i].tot
        index=i

a[index].disp()
    
#for i in range(0,n):
    #a[i].disp()
    
    
        
