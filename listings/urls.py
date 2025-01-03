from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path("about/", views.about, name='about'),
    path('investment', views.investment, name='investment'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
