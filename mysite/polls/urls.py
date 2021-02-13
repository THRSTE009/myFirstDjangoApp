from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    #path() has four arguments:  (route, view, kwargs, name). The last two are optional.  
    #route --> is a string that contains a URL pattern.
    #view --> The specified view function is called with an HttpRequest obejct. E.g. index() inside view.py.
    #kwargs --> is am arbitrary keyword arguments that can be passed in a dictionary to the target view.
    #name --> The name that you give the URL.
]