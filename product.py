
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_value(self) -> float:
        return self.price * self.quantity


def most_expensive(products: list[Product]) -> Product:
    if not products:
        raise ValueError("Product list is empty")

    expensive = products[0]

    for product in products:
        if product.price > expensive.price:
            expensive = product

    return expensive


if __name__ == "__main__":
    products = [
        Product("Laptop", 1200.0, 2),
        Product("Mouse", 25.0, 3),
        Product("Keyboard", 60.0, 2)
    ]

    for product in products:
        print(f"{product.name}: {product.total_value()} AZN")

    best = most_expensive(products)

    print(f"Most expensive product: {best.name}")
