class Laptop:
    def __init__(self,name,model_name,price):
        self.name=name
        self.model_name=model_name
        self.price=price
    def info(self):
        return f"LAPTOP NAME IS {self.name} MODEL IS {self.model_name} AND PRICE IS {self.price} "
class Mlaprop(Laptop):
    def __init__(self,name,model_name,price,ram,internal_hard,processor):
        Laptop.__init__(self,name,model_name,price)
        self.ram=ram
        self.internal_hard=internal_hard
        self.processor=processor
p0=Laptop('Dell','au4dt31',30000)
p1=Mlaprop('Apple','tekde2',150000,'8GB','1TB','4.0GHZ')
print(p1.info())
print(p0.info())
input()