from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Adressee, Category, Product


def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(
            include_self=True
        )
    )
    return render(
        request, "store/category.html", {"category": category, "products": products}
    )


def adressee_list(request, adressee_slug=None):
    adressee = get_object_or_404(Adressee, slug=adressee_slug)
    products = Product.objects.filter(
        adressee__in=Adressee.objects.get(name=adressee_slug).get_descendants(
            include_self=True
        )
    )
    return render(
        request, "store/adressee.html", {"adressee": adressee, "products": products}
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})


class Search(ListView):
    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
