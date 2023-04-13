# define main class
class A:
    def suara(self):
        print("")

# define sub-class
class C(A):
    def suara(self):
        print("roar")

class D(A):
    def suara(self):
        print("meong")

# execute
obj_c = C()
obj_c.suara()  # Output: roar

obj_d = D()
obj_d.suara()  # Output: meong
