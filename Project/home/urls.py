from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name = 'home'),
    path("join/", views.joinaction, name = 'joinaction'),
    path("login/", views.loginaction, name = 'loginaction'),
    path("logout/", views.logoutaction, name='logout_action'),
    path("about/", views.about, name = 'about'),
    path('emp', views.emp),  
    path('show/',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)