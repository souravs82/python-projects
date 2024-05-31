
from django.urls import include, path
from authentication import views 
from .views import logout_user

urlpatterns = [
    path('register_cus/',views.register_user ,name='register_cus'),
    path('login_page',views.login_page, name='login_page'),
    path('logout/', logout_user, name='logout'),



    
]
