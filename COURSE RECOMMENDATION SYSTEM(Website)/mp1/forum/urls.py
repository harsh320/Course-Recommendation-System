from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic import RedirectView
from . import views
urlpatterns = [

    path('index/',views.index,name='index'),

]