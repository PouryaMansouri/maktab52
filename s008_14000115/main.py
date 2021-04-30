class User:
    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    phone: int


class Location:
    lat: int
    lng: int
    address: str


class Customer(User):
    location: Location
    passcode: str
    wallet: int


class Seller(User):
    seller_id = int
    shop_name: str
    rank: int
    stuffs: dict


class Product:
    name: str
    price: int
    tag: str

    def __init__(self, name: str, price: int, tag: str):
        self.name: name
        self.price: price
        self.tag = tag


class Cart:
    product_list: list
    count: int
    customer: Customer
    final_price: int

    def __init__(self, customer: Customer):
        self.customer = customer
        self.product_list = list()
        self.final_price = 0

    def add_product(self, product: Product):
        self.product_list.append(product)
        self.count += 1

    def del_product(self, product: Product):
        if product in self.product_list:
            self.product_list.remove(product)
            self.count -= 1

    def final_price(self):
        for item in self.product_list:
            self.final_price += item.price
        return self.final_price
