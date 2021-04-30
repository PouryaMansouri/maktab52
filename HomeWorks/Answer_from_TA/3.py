class A:
    def do_job(self, s='', n=0):
        if isinstance(self, (E, C)):
            super().do_job(s=s, n=n)
        print('I am walking ...')


class Z:
    def do_job(self, n, s=''):
        if isinstance(self, F):
            super().do_job(s, n)
            print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')
        elif isinstance(self, (E, C)):
            print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')
        else:
            print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')


class B(A):
    def do_job(self, s, n=0):
        super().do_job(s=s, n=n)
        print(f'I am printing your string : "{s}"')


class C(A, Z):
    def do_job(self, n, s=''):
        super().do_job(s, n)
        print('I am jumping ...')


class D(B):
    def do_job(self, s, n=0):
        super().do_job(s, n)
        print('I am speaking ...')


class E(D, C):
    def do_job(self, s, n):
        super().do_job(s, n)
        print('I am laughing ...')


class F(Z, B):
    def do_job(self, s, n):
        super().do_job(s=s, n=n)
        print('I am playing ...')


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(n=3)

print()
obje = E()
obje.do_job('Python', 5)

print()
objf = F()
objf.do_job('Python', 6)

print("*************************************************************")
objb = B()
objb.do_job('python')

print()
objc = C()
objc.do_job(n=6)

print()
objd = D()
objd.do_job('python')
