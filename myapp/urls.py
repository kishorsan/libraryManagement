from django.urls import path, re_path as url
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('', views.login, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('passChange/', views.password, name='password'),
    path('books/', views.home, name='home'),
    url('detail/(?P<id>\d+)/$', views.detail, name='detail'),
    path('insert/', views.insertData, name='insert'),
    # path('delete/(?P<id>\d+)/$', views.deleteData, name='delete'), alternatives for the below urls
    # path('update/(?P<id>\d+)/$', views.updateData, name='update'),
    # url('detail/(?P<id>\d+)/$', views.detail, name='detail'),
    path('delete/<int:id>/', views.deleteData, name='delete'),
    path('update/<int:id>/', views.updateData, name='update'),
]