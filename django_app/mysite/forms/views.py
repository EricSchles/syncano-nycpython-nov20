from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from forms.models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'forms/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last give published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'forms/detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'forms/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'forms/detail.html', {
            'question':p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("forms:results", args=(p.id,)))


