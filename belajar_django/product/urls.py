from django.urls import path 

from .views import category_view, status_view, product_view

urlpatterns = [
    path("product/", product_view.product_index, name="product_list"),
    path("product/create/", product_view.product_create, name="product_create"), # Handle GET & POST
    path("product/<int:id>/update/", product_view.product_update, name="product_update"), # Handle GET & POST
    path("product/<int:id>/delete/", product_view.product_delete, name="product_delete"), # Handle DELETE

    path("category/", category_view.category_index, name="category_list"),
    path("category/create/", category_view.category_create, name="category_create"), # Handle GET & POST
    path("category/<int:id>/update/", category_view.category_update, name="category_update"), # Handle GET & POST
    path("category/<int:id>/delete/", category_view.category_delete, name="category_delete"), # Handle DELETE
    
    path("status/", status_view.status_index, name="status_list"),
    path("status/create/", status_view.status_create, name="status_create"), # Handle GET & POST
    path("status/<int:id>/update/", status_view.status_update, name="status_update"), # Handle GET & POST
    path("status/<int:id>/delete/", status_view.status_delete, name="status_delete"), # Handle DELETE
]