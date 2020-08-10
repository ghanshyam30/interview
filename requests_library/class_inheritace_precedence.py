class A:
    def my_funct(self):
        print("This is from class A")

class B:
    def my_funct(self):
        print("This is from class b")

class C(B, A):
    def __init__(self):
        print("inheritance precedence goes from left to write as mentioned in class definition")

c = C()
c.my_funct()