class Car:
    def __repr__(self):
        return self.__class__.__name__


class Peugeot(Car):
    def __repr__(self):
        return self.__class__.__name__

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

if __name__ == '__main__':
    print('Hello from models.py module')
