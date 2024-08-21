class A:
    def __init__(self):
        print("I Am Base Class")


class B(A):
    def show(self):
        print("I Am Derived class")


ob=B()
ob.show()
