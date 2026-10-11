from enum import Enum


class VendingMachineCodes(Enum):
    SUCCESS = 0
    PRODUCT_NOT_FOUND = 1
    INSUFFICIENT_FUNDS = 2
    AVAILABLE = 3
    UNAVAILABLE = 4


class Product:
    def __init__(self, product_id, price, quantity, name=""):
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.name = name

class VendingMachine:
    def __init__(self):
        self.funds = 0
        self.products = {}
        self.status = VendingMachineCodes.AVAILABLE

    def add_product(self, product: Product) -> bool:
        if product.product_id in self.products:
            return False

        self.products[product.product_id] = product
        return True

    def insert_money(self, amount) -> None:
        self.funds += amount

    def purchase(self, product_id) -> VendingMachineCodes:
        if product_id not in self.products:
            return VendingMachineCodes.PRODUCT_NOT_FOUND

        if self.products[product_id].price > self.funds:
            return VendingMachineCodes.INSUFFICIENT_FUNDS

        self.products[product_id].quantity -= 1
        self.funds -= self.products[product_id].price
        return VendingMachineCodes.SUCCESS


def main():
    chips = Product(1, 250, 5, "chips")

    vending_machine_1 = VendingMachine()
    vending_machine_1.add_product(chips)


