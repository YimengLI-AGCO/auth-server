from django.urls import path
from .views import homePageView
from .views import ApiEndpoint


urlpatterns = [
    path('', homePageView, name='home'),
    path('api/hello', ApiEndpoint.as_view())
]