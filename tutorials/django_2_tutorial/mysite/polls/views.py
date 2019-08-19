from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_questions])
    context = {
        "latest_question_list": latest_questions
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question
    }

    return render(request, "polls/detail.html", context)

def results(request, question_id):
    return HttpResponse(f"You are viewing {question_id} results")

def vote(request, question_id):
    return HttpResponse(f"You are voting for {question_id}")