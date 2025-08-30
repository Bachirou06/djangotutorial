from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from . models import Question

# Using the httresponse
def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

# using get_object_or_404()
def detailss(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/detail.html", {"question": question })

# Rendering the template using try ... except to raise the hhtp-404
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(request, "poll/detail.html", {"question": question})

def result(request, question_id):
    response = "You're looking at the results of questions %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def indexx(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("poll/index.html")
    context = {"latest_question_list": latest_question_list}
    #output = ";".join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "poll/index.html", context)