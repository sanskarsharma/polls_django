from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic 

from .models import *
# Create your views here.

class HomeView(generic.ListView):
    template_name = "polls/home.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ Return the last five published questions. Note that we are only returning a list(QuerySet object) """
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



# def home(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     # my_template = loader.get_template("polls/home.html")
#     # return HttpResponse(my_template.render(context, request))
#     return render(request, "polls/home.html", context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, "polls/results.html", {
#         'question': question
#     })
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST.get("choice"))
    except(KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html", {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=[question_id]))
    
