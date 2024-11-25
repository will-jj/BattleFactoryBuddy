from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setcalc', views.setcalc, name='setcalc'),    
    path('speedcalc',views.speedcalc, name='speedcalc'),
    path('switchincalc',views.switchincalc, name='switchincalc'),
    path('teambuilder',views.teambuilder, name='teambuilder'),
]