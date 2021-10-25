from django.contrib import admin
from django.urls import include, path

from mysite import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup')
]
