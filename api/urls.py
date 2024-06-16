from django.urls import path
from ninja import NinjaAPI
from .schemas import ProductSchema, ProductOutput
from .models import Product

api = NinjaAPI()


@api.get("/products", response=list[ProductOutput])
def list_product(request):
    products = Product.objects.all()
    return products


@api.get("/products/{id}", response=ProductOutput)
def get_product(request, id: int):
    product = Product.objects.get(id=id)
    return product


@api.post("/products", response=ProductOutput)
def create_product(request, item: ProductSchema):
    new_product = Product.objects.create(
        name=item.name, description=item.description, price=item.price)
    return new_product


@api.put("/products/{id}")
def update_product(request):
    pass


@api.delete("/products/{id}")
def delete_product(request):
    pass


urlpatterns = [
    path("", api.urls),
]
