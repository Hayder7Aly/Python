class Phone:
    def __init__(self,phone_name,model_name,price):
        self.phone_name=phone_name
        self.model_name=model_name
        self.price=price
    @classmethod 
    def class_1(cls):
        return f"Your class name is {cls.__name__}"
    @property
    def property_1(self):
        return f'your name is {self.phone_name}'
    @staticmethod
    def staticmethod_1():
        return f'Your are called staticmethod decorator:'
p1=Phone('Oppo','F5 Youth',30000)
print(p1.class_1())
print(p1.property_1())
print(p1.staticmethod_1())
input()