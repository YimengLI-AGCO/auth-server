from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView


def homePageView(request):
    return HttpResponse('index.html')


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
