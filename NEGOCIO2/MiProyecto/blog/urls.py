from . import views
from django.urls import path

urlpatterns = [
    #path('blog', views.PostList.as_view(), name='bloghome'),
    path('blog', views.lista_de_posts, name='bloghome'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]