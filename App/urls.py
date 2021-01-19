from django.urls import path

from App import views

urlpatterns = [
    path('login/', views.userlogin),
    path('regist/', views.userregist),
]
