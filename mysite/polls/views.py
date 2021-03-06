from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Voie, Site, Secteur


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class VoieView(generic.ListView):
    template_name = 'polls/voie.html'
    context_object_name = 'voie_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Voie.objects.order_by('name')


class SiteView(generic.ListView):
    template_name = 'polls/sites.html'
    context_object_name = 'sites_list'

    def get_queryset(self):
        return Site.objects.order_by('name')


class SecteurView(generic.ListView):
    template_name = 'polls/secteurs.html'
    context_object_name = 'secteurs_list'

    def get_queryset(self):
        return Secteur.objects.order_by('name')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
