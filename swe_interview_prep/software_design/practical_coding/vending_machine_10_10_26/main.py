"""
Nayeel Imtiaz
10-10-26

Chatgpt give practical coding prompt (45 minutes):
- Vending Machine supporting functionality for the following:
    - `add_product`
    - `insert_money`
    - `purchase`

Timeline:
    1) Nayeel's Initial implementation (30 minutes)
    2) Nayeel's final clean up based on Chatgpt midpoint feedback (15 minutes)

Reflection:
    - Honestly, not too bad of an implementation, but there is definitely room for improvement.

    - What went well:
        - Defined separate entities such as `Product` and `VendingMachine`
        - Used enums to define success/error codes
        - `purchase` operation had strong failure checking and seems well developed.
    - What could be improved:
        - `insert_money` operation is too trivial and more prone to error:
            - A customer is not prevented from inserting funds during an invalid state
            (when vending machine is dispensing snack for example).
            - Customer can potentially put invalid currency inside. A stronger
            approach can be to check Customer passed in valid form of payment
            (Money type object like Apple Pay, Credit card, etc which all
            perhaps implements an interface like `PaymentMethod`.
        - `add_product` uses boolean return value instead of an enum like
        those defined in `VendingMachineCodes`
        - Understand requirements faster
            - Slightly faster implementation would be ideal so I have more time to do
            more testing and add more foods for the vending machine.
            - In a real interview setting, interviewer will ask clarification questions
            more which could take up a little time.
            - Understanding requirements and aligning on functional and non-functional
            requirements quicker is key, not necessarily typing faster code.
    - Next steps:
        - Do more practice problem in a time boxed setting. Real interviews won't give
        you 2-3 hours to code up something perfect.
        - However, something pretty substantial is likely expected. So understanding
        and clarifying requirements as soon as possible is key to have more time
        for better end results.
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
