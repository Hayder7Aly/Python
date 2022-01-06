class Mobile:
    def __init__(self,name):
        self.name=name
class Mobiel_store:
    def __init__(self):
        self.mobiles=[]
    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('Haider ali Jutt')
mobo=Mobile('hawiea')
new='samsung galaxy'
mobo_store=Mobiel_store()
mobo_store.add_mobiles(mobo)
print(mobo_store.mobiles)
input()