# urls.py
from django.urls import path
from .views import CategoryProductsView, category_list, order_detail, order_list, product_detail, product_list,home,ProductDetailView

urlpatterns = [
    path('', home, name='home'),
    path('categories/', category_list, name='category_list'),
   # path('categories/<int:category_id>/', category_products, name='category_detail'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='prod_detail'),
    path('categories/<str:category>/', CategoryProductsView.as_view(), name='category_products'),
    

]
