from django.http import HttpResponse

#To call the view, map it to a URL via the URLconf.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")