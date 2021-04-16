class Object:
    def do_job(self, s=None, n=None):
        return "  "


class A(Object):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + "I am walking ..."
        #
        # print('I am walking ...')


class Z(Object):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + f'I am counting from 1 to {n}:  {list(range(1, n + 1))}'
        #
        # print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')


class B(A):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + f'I am printing your string : "{s}"'
        #
        # super().do_job(s=s, n=n)
        # print(f'I am printing your string : "{s}"')


class C(A, Z):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + "I am jumping ..."
        #
        # super().do_job(s=s, n=n)
        # print('I am jumping ...')


class D(B):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + "I am speaking ..."
        #
        # super().do_job(s)
        # print('I am speaking ...')


class E(D, C):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + "I am laughing ..."
        # return super().do_job(s=s, n=n)
        # print('I am laughing ...')


class F(Z, B):
    def do_job(self, s=None, n=None):
        return super().do_job(s=s, n=n) + "\n" + "I am playing ..."
        # print('I am playing ...')


"""
1. change all of do_job to the same syntax
2. change all do_job to return super instead of print or call 
3. add class Object to parent off class A and class Z 
"""

obja = A()
print(obja.do_job())

print()
objz = Z()
print(objz.do_job(n=3))

print()
obje = E()
# print(E.mro())
print(obje.do_job(s='Python', n=5))

print()
objf = F()
# print(F.mro())
print(objf.do_job(s='Python', n=6))
