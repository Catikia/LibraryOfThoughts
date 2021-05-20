from django.urls import path
#from . import views
from .views import HomeView, BlogpostDetailView, AddThoughtView, EditThoughtView, RemoveThoughtView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path("blogpost/<int:pk>", BlogpostDetailView.as_view(), name="blogpost-detail"),
    path("add_category", AddCategoryView.as_view(), name="add_category"),
    path("add", AddThoughtView.as_view(), name="add"),
    path("blogpost/edit/<int:pk>", EditThoughtView.as_view(), name="edit_thought"),
    path("blogpost/<int:pk>/delete", RemoveThoughtView.as_view(), name="remove_thought"),
    path("category/<str:cats>", CategoryView, name="category"), #cats is short for category
    path("category-list/", CategoryListView.as_view(), name="category-list"),
]
