class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calc_circumfrence(self):
        return 2*Circle.pi*self.radius
    def calc_area(self):
        return Circle.pi*self.radius**2
r_1=int(input('Enter the radius:'))
c=Circle(r_1)
c1=Circle(r_1)
c1.pi=1
print('The circumfrence of radius is :',c.calc_circumfrence())
print('The area of radius is :',c1.calc_area())
input()