from django.urls import path, include
from question_bank import views

urlpatterns = [
    path('danxuan/', views.danxuan),
    path('first/', views.first)
]
