class Student:
    def __init__(self,name,roll_no,clas):
        self.name=name
        self.roll_no=roll_no
        self.clas=clas
    def info(self):
        return f"THE STUDENT NAME IS '{self.name}' ROLL NO IS '{self.roll_no}' AND CLASS NAME IS '{self.clas}' "
class Rstudent(Student):
    def __init__(self,name,roll_no,clas,father_name,ph_no):
        Student.__init__(self,name,roll_no,clas)
        self.father_name=father_name
        self.ph_no=ph_no
p0=Student('Haider Ali Jutt',15,'9Th (A)')
p1=Rstudent('Ali Raza',19,'B.S.C','Bahadar Ali','id')
print(p0.info())
print(p1.info())
input()