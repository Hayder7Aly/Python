class Laptop:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def info(self):
        return f"\tYOUR LAPTOP NAME IS '{self.name}' AND MODEL IS '{self.model}' "
    def original_price(self,num):
        discount=(num/100)*self.price
        o_r=self.price-discount
        print(f'\tTHE PRICE OF LAPTOP IS WITH OUT DISCOUNT Rs.{self.price}')
        return f'\tTHE ORIGANAL PRICE IS Rs.{o_r}'
name=input('\nEnter the name of laptop :')
model=input('Enter the model of laptop :')
price=int(input('Enter the price of laptop :'))
p1=Laptop(name,model,price)
print(p1.info())
num=int(input('Enter the discount of percentage price Rs :'))
print(p1.original_price(num))
input()