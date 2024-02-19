"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views # to import views module, so that
#any function in the views folder can be called

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('home/', views.home),
    # this views.home implies calling of the home function in views file
    
    path ('', views.home, name="home"), # name can be anything
    # now this path can be referred to as "name"
    # blank shows that it is the actual home page (default home page = home function is automatically triggerred)

    # all requests comes to this page first : urls.py in the project folder
    # therefore, all the requests are redirected from here
    path('employee/', include('employee.urls'))
    # any request that comes must be REDIRECTED to "employee" app
    # whenever user types in '/employee/' we redirect it to urls.py within the app folder

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# this static() function is to facilitate the user uploaded files
# for eg: the images uploaded by the user
