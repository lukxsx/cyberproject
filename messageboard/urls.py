from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.threadview, name='threadview'),
    path('addthread/', views.addthread, name='addthread'),
    path('<int:thread_id>/add/', views.addpost, name='addpost'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register_view, name='register_view'),
    path('delpost/', views.deletepost, name='deletepost'),
]
