from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import roles_view
urlpatterns = [
    path ('login/', TokenObtainPairView.as_view()),
    path ('roles/', roles_view),
]