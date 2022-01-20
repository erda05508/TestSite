from .models import Category, Adressee


def categories(request):
    return {"categories": Category.objects.filter(level=0)}


def adressees(request):
    return {"adressees": Adressee.objects.filter(level=0)}
