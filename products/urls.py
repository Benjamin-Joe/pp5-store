"Products Urls"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('category/<category>/', views.CategoryList.as_view(), name='category')
]
