class Add:
    def __init__(self,first_number,second_number):
        self.first_number=first_number
        self.second_number=second_number
    def total(self):
        return f"First number is {self.first_number} and Second number is {self.second_number} and Totla is {self.first_number+self.second_number}"
class Secadd(Add):
    def __init__(self,first_number,second_number,third_number):
        Add.__init__(self,first_number,second_number)
        self.third_number=third_number
    def sec_total(self):
        return f"Totla in three number is {self.first_number+self.second_number+self.third_number}"
n=int(input('Enter 1st number :'))
n2=int(input('Enter 2nd number :'))
n3=int(input('Enter 3rd number :'))
p1=Add(n,n2)
p2=Secadd(n,n2,n3)
print(p1.total())
print(p2.sec_total())
input()