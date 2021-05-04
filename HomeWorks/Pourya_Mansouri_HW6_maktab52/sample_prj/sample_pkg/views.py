from .models import Car, Peugeot
# from models import Car, Peugeot


class CarView:
    model = Car

    def show(self):
        print(self.model())


class PeugeotView:
    model = Peugeot

    def show(self):
        print(self.model())

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))
if __name__ == '__main__':
    print('Hello from views.py module')
