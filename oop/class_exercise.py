class Laptop:
    def __init__(self,brand_name,price,model_name):
        self.brand_name=brand_name
        self.price=price
        self.model_name=model_name
        self.laptop_full_quality=brand_name+' '+model_name+' '+price
p1=Laptop('DELL','85000','4TH GENERATION')
p2=Laptop('Hp','70000','3rd GENERATION')
print(p1.laptop_full_quality)
print(p2.laptop_full_quality)
input()