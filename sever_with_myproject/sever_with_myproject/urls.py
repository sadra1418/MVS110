
from django.contrib import admin
from django.urls import path
from api.views import api , test , main_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , api ),
    path( 'test/' , test),
    path('' , main_app)
]
