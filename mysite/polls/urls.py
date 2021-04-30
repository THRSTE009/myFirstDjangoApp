from django.urls import path

from . import views

# If you want to change the URL of the polls detail view to something else,
# perhaps to something like polls/specifics/12/ instead of doing it in the template (or templates) you would change it in polls/urls.py:
app_name = 'polls'
    # How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?
    # The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an 'app_name' to set the application namespace.
urlpatterns = [

    # Added for generic views.
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('charts/', views.chartsView, name='charts'),

    # Old method for adding urls.
    #path('', views.index, name='index'), # ex: /polls/
    #path('<int:question_id>/', views.detail, name='detail'), # ex: /polls/5/
        # the 'name' value as called by the {% url %} template tag
        # Using angle brackets �captures� part of the URL and sends it as a keyword argument to the view function.
    #path('<int:question_id>/results/', views.results, name='results'), # ex: /polls/5/results
    #path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote

    # path() has four arguments:  (route, view, kwargs, name). The last two are optional.
    # route --> is a string that contains a URL pattern.
    # view --> The specified view function is called with an HttpRequest obejct. E.g. index() inside view.py.
    # kwargs --> is am arbitrary keyword arguments that can be passed in a dictionary to the target view.
    # name --> The name that you give the URL.
]
