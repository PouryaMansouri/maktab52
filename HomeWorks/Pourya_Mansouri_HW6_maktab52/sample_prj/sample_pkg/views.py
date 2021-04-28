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


if __name__ == '__main__':
    print('Hello from views.py module')
