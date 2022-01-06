class Phone:
    def __init__(self,phone_name,model_name,price):
        self.phone_name=phone_name
        self.model_name=model_name
        self.price=price
    def info(self):
        return f"Your Phone Full Name Is {self.phone_name}{self.model_name}"
    def price(self):
        return f"Your Phone Price is {self.price}"
class Smartphone(Phone):
    def __init__(self,phone_name,model_name,price,ram,internal_memory,rare_camera):
        # super().__init__(phone_name,model_name,price)
        Phone.__init__(self,phone_name,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rare_camera=rare_camera
# name=int(input('Enter the name of phone :'))
p0=Phone('Nokia','220',1000)
p1=Smartphone('apple','6',100000,'4GB','64GB','3.3pixel')
print(p1.info())
print(p0.info())
input()