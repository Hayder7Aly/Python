class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def info(self):
        return f"Your Phone Name Is {self.name} And Model is {self.model}"
class Geneticphone(Phone):
    def __init__(self,name,model,price,brand,ram):
        Phone.__init__(self,name,model,price)
        self.brand=brand
        self.ram=ram
    def info(self):   
        return f"{self.name} {self.model} and price is {self.price}"
class Smartphone(Geneticphone):
    def __init__(self,name,model,price,brand,ram,rom,front_camera):
        Geneticphone.__init__(self,name,model,price,brand,ram)
        self.rom=rom
        self.front_camera=front_camera
p1=Smartphone('OppO','au3d3','23000Rs.','F5','4GB','64GB','12.4px')
p2=Geneticphone('Sumsung','t3d3jd','10000RS.','j7','2GB')
print(isinstance(p2,Phone))
print(issubclass(Phone,Smartphone))
input()
