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
        return f"your brand is {self.brand} and front-camera {self.front_camera}"
class Smartphone_2(Smartphone):
    def __init__(self,name,model_name,price,ram,rare_camera,internal_hardisk,brand,front_camera):
        Phone.__init__(self,name,model_name,price)
        self.brand=brand
        self.front_camera=front_camera
p1=Smartphone_2('OnePlus','F5',50000,'5GB','8.0Pixel','64GB','thw','10MP')
print(p1.full_info())
input()