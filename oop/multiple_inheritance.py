class A:
    def class_a_method(self):
        return f"i 'm class method A"
    def hello(self):
        return f" Hello class A"
class B:
    def class_b_method(self):
        return f"i 'm class method B"  
    def hello(self):
        return f"Hello from class B"
class C(A,B):
    pass
instance=C()
# print(instance.class_a_method())
# print(instance.class_b_method())
# print(instance.hello())
print(help(C))
print(C.mro())
input()