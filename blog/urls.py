from django.urls import path
from . import views 

app_name = 'blog'

urlpatterns = [
path('',views.Home,name='index'),
path('create/',views.Create,name='create'),
path('<int:id>/',views.Detail)
]


""" path('update/<str:id>/',views.Update,name='update_post'),
path('delete/<str:id>/',views.Delete,name='delete_post'), """
