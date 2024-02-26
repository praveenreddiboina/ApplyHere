from django.urls import path
from .views import userregistration, userlogin, profileview,userlogout
urlpatterns = [
    path('registration/', userregistration.as_view(), name="registration"),
    path('login/', userlogin.as_view(), name="login"),
     path('logout/', userlogout.as_view(), name="logout"),
    path('viewprofile/', profileview.as_view(), name="viewprofile"),
]