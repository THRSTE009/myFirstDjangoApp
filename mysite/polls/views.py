from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Question

# Views must return either an HttpResponse object, containnig the content for the requested page, or raise an exception, such as Http404.

# To call the view, map it to a URL via the URLconf.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list } # Context is a dictionary mapping template variable names to Python objects.
    return render(request, 'polls/index.html', context) # render(request object, template name, dictionary(optional))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id) #if a question with this idea does not exist then the view will raise the Http404 exception.
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    #faster method to raise Http404 is:
    question = get_object_or_404(Question, pk=question_id)
        # get_object_or_404 acts as a helper function.
        # It's used to decouple the 'model layer' from the 'view layer'. I.e. The model API raises Http404.
        # get_object_or_404('takes a Django model', 'takes an arbitrary number of keyword arguments')
        # these arguments are passed to the model's manager get() which raises Http404 if the object does not exist.
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
