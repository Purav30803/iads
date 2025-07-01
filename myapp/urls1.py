# project_folder/urls.py
from django.urls import path, include
from myapp import view1,detail_view

urlpatterns = [
    path('about/', view1.about),
    path('<int:book_id>', detail_view.detail)

]
