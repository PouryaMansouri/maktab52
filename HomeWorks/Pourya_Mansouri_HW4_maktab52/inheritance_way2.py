class A:
    def do_job(self, s=None, n=None):
        if isinstance(self, E):
            super().do_job(n=n, s=s)
        print('I am walking ...')


class Z:
    def do_job(self, s=None, n=None):
        if isinstance(self, F):
            super(Z, self).do_job(n=n, s=s)
        print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')


class B(A):
    def do_job(self, s=None, n=None):
        super().do_job(n=n, s=s)
        print(f'I am printing your string : "{s}"')


class C(A, Z):
    def do_job(self, s=None, n=None):
        super().do_job(n=n, s=s)
        print('I am jumping ...')


class D(B):
    def do_job(self, s=None, n=None):
        super().do_job(s=s, n=n)
        print('I am speaking ...')


class E(D, C):
    def do_job(self, s=None, n=None):
        super().do_job(s=s, n=n)
        print('I am laughing ...')


# TODO: how use **kwarg
class F(Z, B):
    def do_job(self, s=None, n=None):
        super().do_job(s=s, n=n)
        print('I am playing ...')


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(n=3)

print()
print(E.mro())
print()
obje = E()
obje.do_job(s='Python', n=5)

print()
objf = F()
print(F.mro())
print()
objf.do_job('Python', 6)
