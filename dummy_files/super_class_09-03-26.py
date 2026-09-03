class Vehicle:
    def __init__(self, name: str):
        self.name = name

class Lexus(Vehicle):
    def __init__(self, name: str):
        super().__init__(name)
        self.lexus = True

    def __str__(self):
        return f"{self.name} {self.lexus}"

def main():
    l = Lexus("ES300")
    print(l)


if __name__ == "__main__":
    main()
