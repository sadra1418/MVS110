
from django.contrib import admin
from django.urls import path
from api.views import api , test , main_app , google_verification




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , api ),
    path( 'test/' , test),
    path('' , main_app),
    path('googleccc612f328fb14c8.html', google_verification),
    
]

