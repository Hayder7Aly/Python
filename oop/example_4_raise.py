class Laptop:
    def __init__(self,name):
        self.name=name
class Rlaptop:
    def __init__(self):
        self.laptops=[]
    def store(self,new_laptop):
        self.laptops.append(new_laptop)
lap=Laptop('dell')
rlap=Rlaptop()
new='Hp'
rlap.store(new)
print(rlap.laptops)
input()