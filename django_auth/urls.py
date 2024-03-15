
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import include, path
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return HttpResponse('Main Page')

@login_required
def about(request):
    return HttpResponse('about Page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('about', about, name="about"),
    path('accounts/', include('accounts.urls'))
]
