from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]
