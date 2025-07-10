from django.urls import path
from myapp import views,view1

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
path('<int:book_id>/', views.detail, name='detail'),

    path('feedback/', views.getFeedback, name='feedback1'),
path('findbooks/', views.findbooks, name='findbooks'),
path('place_order/', views.place_order, name='place_order'),



]
