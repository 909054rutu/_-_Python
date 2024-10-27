#A) Write a Python class named Student with two attributes student_name, marks.
#Modify the attribute values of the said class and print the original and modified values
#of the said attributes.

class stude:
    def accept(self,name,marks):
        self.name=name
        self.marks=marks

        name="swami"
        marks=99

        print("original name",self.name)
        print("original marks",self.marks)
        print("modify name",name)
        print("modify marks",marks)

ob=stude()
ob.accept("sham",80)
