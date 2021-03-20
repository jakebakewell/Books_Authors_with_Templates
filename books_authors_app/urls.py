from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<int:id_num>', views.books),
    path('authors/<int:id_num>', views.authors_specific),
    path('process_book', views.process_book),
    path('process_author', views.process_author),
    path('add_author', views.add_author),
    path('add_book', views.add_book),
]