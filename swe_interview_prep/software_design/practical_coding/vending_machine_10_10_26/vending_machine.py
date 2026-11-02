"""
Nayeel Imtiaz
10-10-26

Chatgpt give practical coding prompt (45 minutes):
- Vending Machine supporting functionality for the following:
    - `add_product`
    - `insert_money`
    - `purchase`
"""

from enum import Enum

class Foods(Enum):
    CHIPS = 1

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

    def __repr__(self):
        return (
            f"product_id = {self.product_id}, " 
            f"price = {self.price}, "
            f"quantity = {self.quantity}, "
            f"name = {self.name}"
        )

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
        if (
                product_id not in self.products
                or self.products[product_id].quantity <= 0
        ):
            return VendingMachineCodes.PRODUCT_NOT_FOUND

        if self.products[product_id].price > self.funds:
            return VendingMachineCodes.INSUFFICIENT_FUNDS

        self.products[product_id].quantity -= 1
        self.funds -= self.products[product_id].price
        return VendingMachineCodes.SUCCESS

    def __repr__(self):
        return (
            f"funds = {self.funds}, "
            f"products = {self.products}, "
            f"status = {self.status}"
        )


def main():
    chips = Product(Foods.CHIPS, 250, 5, "chips")
    print("CREATE CHIPS")
    print(chips)
    print()

    print("CREATE VENDING MACHINE")
    vending_machine_1 = VendingMachine()
    print(vending_machine_1)
    print()

    print("ADD CHIPS TO VENDING MACHINE")
    vending_machine_1.add_product(chips)
    print(vending_machine_1)
    print()

    print("ADD $3 TO VENDING MACHINE")
    vending_machine_1.insert_money(300)
    print(vending_machine_1)
    print()

    for _ in range(2):
        print("PURCHASE CHIPS FROM VENDING MACHINE")
        print(vending_machine_1.purchase(Foods.CHIPS))
        print(vending_machine_1)
        print()


if __name__ == '__main__':
    main()
