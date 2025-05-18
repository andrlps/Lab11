from dataclasses import dataclass
from model.product import Product


@dataclass
class Edge:
    p1: Product
    p2: Product
    weight: int