from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView

urlpatterns = [
 path('category_list/', CategoryListView.as_view(), name='category_list'),
 path('category_create/', CategoryCreateView.as_view(), name='category_create'),
 path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
 path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
 path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete')
]
