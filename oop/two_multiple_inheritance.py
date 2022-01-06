class A:
    def string(self):
        return f"First string class is A"
class B:
    def string_1(self):
        return f"Second string class is B"
class C(A,B):
    def string_3(self):
        return f"Third string class is C"
    pass
instance=C()
print(instance.string())
print(instance.string_1())
print(instance.string_3())
input()