from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/add")
def add(request, a: int = 2, b: int = 3):
    return {"result": a + b}


urlpatterns = [
    path("", api.urls),
]
