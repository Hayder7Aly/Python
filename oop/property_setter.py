class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self._price=max(price,0)
    def info(self):
        return f"{self.name} {self.model} and price is {self._price}"
p1=Phone('Nokia','1100',-1000)
p1._price=-14
print(p1._price)
print(p1.info())

    