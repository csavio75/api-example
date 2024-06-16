from ninja import Schema


class ProductSchema(Schema):
    name: str
    description: str
    price: float


class ProductOutput(Schema):
    id: int
    name: str
    description: str
    price: float
