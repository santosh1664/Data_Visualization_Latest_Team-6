from django.urls import path
from . import views
from django.urls import path, include
from home.dash_apps.finished_apps import SimpleGraph

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cards/', views.cards, name='cards'),
    path('charts/', views.charts, name='charts'),
    path('reset-password/', views.resetpwd, name='reset-password'),
    path('tables/', views.tables, name='tables'),
    path('upload-data/', views.upload_data, name='upload_data'),
    path('audio/<filename>', views.serve_audio, name='serve_audio'),
    path('login/', views.login , name='login'),
    path('logo/', views.logo , name='logo'),
    path('readCookies/', views.readCookies , name='readCookies'),
]
