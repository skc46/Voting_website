from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

# def index(request):  # commented for creating class based view, see below
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context ={'latest_question_list': latest_question_list}
    
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):  # equivalent of above function
    template_name = 'polls/index.html'
    context_object_name= 'latest_question_list'  # to change the default name
    
    def get_queryset(self):
        """Return the last five published questions (
        not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte = 
                                       timezone.now()).order_by('-pub_date')[:5]
           # lte means less than or equal to                            

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
        
#     context = {'question':question}    
#     return render(request, 'polls/detail.html', context)
""" CLass based view of detail"""
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    """we want to avoid users from guessing future questions even if
       they don't appear"""
       
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
# def results(request, question_id):

#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
        # the request.POST['choice'] returns the ID of the selected choice
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        context = {
        'question': question,
        'error_message': "You didn't select a choice.",
            }    
        return render(request, 'polls/detail.html', context)
    
    else:
        selected_choice.votes +=1
        selected_choice.save()
        
        # Always return an HttpResponseRedirect after succesfully dealing 
        # with POST data. This prevents data from being posted twice
        # if a user hits the Back button.
        
        return HttpResponseRedirect(reverse('polls:results', 
                                            args=(question.id,)))
      # The reverse() function is given the name of a view
      # that we want to pass control to and the variable 
      # portion of the URL pattern that points to that view.
      # This means after somebody votes in question, the vote() view
      # redirects to the results page for the question.