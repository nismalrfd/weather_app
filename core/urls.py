from django.urls import path

from core import views

urlpatterns = [
    path('', views.home,name='home'),
    path('get_content', views.get_content, name='get_content'),

]
