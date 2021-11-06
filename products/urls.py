from django.urls import path

from products.views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductCreateView,
    CategoryCreateView,
                            )

urlpatterns = [
    path('', ProductListView.as_view(), name='dashboard'),
    path('product/<str:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<str:pk>/edit/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<str:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product-new/', ProductCreateView.as_view(), name='product-create'),
    path('category-new/', CategoryCreateView.as_view(), name='category-create'),
]



