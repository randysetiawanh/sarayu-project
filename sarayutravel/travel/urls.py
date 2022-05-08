from django.urls import path, re_path

from . import views

app_name = 'travel'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('package/', views.PackageView, name='package'),
    path('about/', views.AboutView, name='about'),
    path('contactus/', views.ContactusView, name='contactus'),
    path('signin/', views.SigninView, name='signin'),
    path('signup/', views.SignupView, name='signup'),
    re_path(r'^package/detail/(?P<idPackage>[\w-]+)/$', views.PackageDetailView, name='signup'),
]
