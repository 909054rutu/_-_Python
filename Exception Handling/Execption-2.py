class NegativeNumber (RuntimeError):
    def __init__ (self,msg):
        self.msg=msg

try:
    n=int(input("Enetr Number"))
    if(n<0):
          raise NegativeNumber("Number is Negative")
    print("Number=",n)
except  NegativeNumber  as e:
    print(e)
