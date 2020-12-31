from django.urls import path
from home import views

# from home import views as home

app_name = 'home'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:post_id>/', views.Post_.as_view(), name='post'),
]
