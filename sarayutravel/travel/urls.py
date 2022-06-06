from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path

from . import views

app_name = 'travel'
urlpatterns = [
    path('', views.IndexView, name='index'),
    re_path(r'^booking/(?P<idDetailOrder>[0-9a-f-]+)/$', views.BookingView, name='booking'),
    re_path(r'^make_payment/(?P<idMakePayment>[\w-]+)/$', views.MakePaymentView, name='makepayment'),
    re_path(r'^process_booking/(?P<idBooking>[\w-]+)/$', views.ProcessBookingView, name='process_booking'),

    path('about/', views.AboutView, name='about'),
    path('contactus/', views.ContactusView, name='contactus'),
    path('signin/', views.SigninView, name='signin'),
    path('signup/', views.SignupView, name='signup'),
    path('package/', views.PackageView, name='package'),
    re_path(r'^package/detail/(?P<idPackage>[\w-]+)/$', views.PackageDetailView, name='packagedetail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)