from .models import Car, Peugeot


class CarView:
    model = Car

    def show(self):
        print(self.model())


class PeugeotView:
    model = Peugeot

    def show(self):
        print(self.model())




print('Hello from views.py module')
