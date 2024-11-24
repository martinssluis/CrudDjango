from django.contrib import admin
from django.urls import include, path
from app_forms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form_modelform, name='home'),
    path('app_forms/', include('app_forms.urls')), #? show the path to app_forms and the app url, and this is used to display the app's page on the web
]
