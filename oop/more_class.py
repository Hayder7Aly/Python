class Phone:
    def __init__(self,name,model_name,price):
        self.name=name
        self.model_name=model_name
        self.price=price
    def info(self):
        return f"Full Name is {self.name} {self.model_name}"
    def price(self):
        return f"Your phone price is {self.price}"
class Smartphone(Phone):
    def __init__(self,name,model_name,price,ram,rare_camera,internal_hardisk):
        Phone.__init__(self,name,model_name,price)
        self.ram=ram
        self.rare_camera=rare_camera
        self.internal_hardisk=internal_hardisk
    def full_info(self):
        return f"Your Phone Hardisk is {self.internal_hardisk}"
class Smartphone_2(Phone):
    def __init__(self,name,model_name,price,brand):
        Phone.__init__(self,name,model_name,price)
        self.brand=brand
    def company(self):
        return f"Your phone brand is {self.brand}"
p0=Phone('Nokia','1100',1000)
p1=Smartphone('OnePlus','F5',50000,'5GB','8.0Pixel','64GB')
p2=Smartphone_2('OppO','F5',30000,'Mac')
print(p2.info())
print(p1.info())
print(p0.info())
input()
