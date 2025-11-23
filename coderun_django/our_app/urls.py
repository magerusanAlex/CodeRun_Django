from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='compass')),
    path('compass/', views.compass_view, name='compass'),
    path('instructions/<int:instruction_id>/', views.instruction_detail_view, name='instruction_detail'),
]