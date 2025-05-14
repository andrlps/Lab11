from dataclasses import dataclass
from model.product import Product


@dataclass
class Arco:
    p1: Product
    p2: Product
    peso: int

    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2