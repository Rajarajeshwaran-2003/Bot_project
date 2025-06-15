from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome_page, name ='welcome'),
    path('chat/', views.chatbot_home, name='chatbot_home'),
    path('get_response/', views.chatbot_response, name='get_response'),  # ✅ Use chatbot_response
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
