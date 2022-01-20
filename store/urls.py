from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='store_home'),
    path('detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('phone/<slug:category_slug>/', views.category_list, name='category_list'),
    path('place/<slug:adressee_slug>/', views.adressee_list, name='adressee_list'),
    path('search/', views.Search.as_view(), name='search'),
]
