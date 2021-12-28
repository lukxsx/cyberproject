from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.threadview, name='threadview'),
    path('addthread/', views.addthread, name='addthread'),
    path('<int:thread_id>/add/', views.addpost, name='addpost'),

]
