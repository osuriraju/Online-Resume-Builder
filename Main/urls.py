from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.Login),
    path('signup', views.Signup),
    path('logout', views.Logout),
    path('dashboard', views.dashboard),
    path('createresume/<int:id>', views.CreateResume),
    path('viewresume/<int:id>', views.ViewResume),
    path('delete/<int:id>', views.deleteResume),
    path('update/<int:id>', views.updateResume),
]