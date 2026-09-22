from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('patients/', include('core.urls.patient')),
    path('doctors/', include('core.urls.doctor')),
    path('appointments/', include('core.urls.appointment')),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
