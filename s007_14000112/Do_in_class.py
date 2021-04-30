class MyClass:
    class_attr = "It's a class Attribute!"

    def __init__(self, x=None):
        self.my_attr = x or "It's my Attribute!"

    def instance_method(self):
        self.class_attr = "MY class_attr modified!"

    @classmethod
    def class_method(cls):
        cls.class_attr = "class_attr modified!"


c1 = MyClass()
c2 = MyClass("salam")
c1.class_method

print(c2.my_attr)