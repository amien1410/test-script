# define main class
class A:
    def suara(self):
        print("")

# define sub-class
class B(A):
    def suara(self):
        print("roar")

class C(A):
    def suara(self):
        print("meong")

# execute
objek_B = B()
objek_B.suara()  # Output: roar

objek_C = C()
objek_C.suara()  # Output: meong
