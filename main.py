class Laptop:

    def __init__(self, brand, model_name, price):
        self.brand = str(brand)
        self.name = str(model_name)
        self.price = float(price)
        self.product_name = brand + " " + model_name

    def apply_discount(self, value):
        self.price -= (self.price * value) / 100
        return self.price
