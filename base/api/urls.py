from django.urls import path
from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView, MyView, MyGetView

urlpatterns = [
    # Define URL pattern for getting available routes
    path('', view=views.get_routes),
    # Define URL pattern for obtaining JWT token
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Define URL pattern for refreshing JWT token
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    # Define URL pattern for getting paragraphs
    path('get/', MyGetView.as_view()),
    # Define URL pattern for adding paragraphs
    path('post/', MyView.as_view())
]
