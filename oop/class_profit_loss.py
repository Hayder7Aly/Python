class Work:
    def __init__(self,kg_of_sugar,price_per_kg,income):
        self.kg_of_sugar=kg_of_sugar
        self.price_per_kg=price_per_kg
        self.income=income
    def info(self):
        profit_loss=self.kg_of_sugar*self.price_per_kg
        if self.income>profit_loss:
            profit=self.income-profit_loss
            return f"Your profit is {profit} Rupees :"
        elif self.income<profit_loss:
            loss=profit_loss-self.income
            return f" Your loss is {loss} rupees :"
        else:
            return f" you have no loss and no profit :"
kg=int(input('Enter the kg of sugar :'))
price=int(input('Enter the price of per kg :'))
income=int(input('Enter the income of sugar stacking :'))
p1=Work(kg,price,income)
print(p1.info())
input()