from django.urls import path, include
from question_bank import views

urlpatterns = [
    path('danxuan/', views.danxuan, name='danxuan'),
    path('tf/', views.tf, name='tf'),
    path('jianda',views.jianda,name='jianda'),
    path('first/', views.first),
    path('ttff/', views.ttff),
    path('jd/',views.jd),
    path('index/', views.index,name='qbindex'),
    path('qblist/',views.qblist,name='qblist'),
    path('zuzu/',views.zuzu,name='zuzu'),

]
