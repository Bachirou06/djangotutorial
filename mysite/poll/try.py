from django.http import Http404
from django.shortcuts import render
from future.backports.http.client import HTTPResponse

from . models import Question
from django.template import loader
def index(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("The question does not exists")
    return render(request, "poll/index.html", {"question": question})
# Use Http response to load the gabarit
def indexx(request, question_id):
    latest_question_list = Question.objects.order_by("-published_id")[:5]
    template = loader.get_template("poll/index.html")
    context = {"latest_question_list": latest_question_list}
    return HTTPResponse(render(request, template, context))
def indexxx(request, question_id):
    latest_question_list = Question.objects.order_by("-published_id")[:5]
    return render(request, "poll/indexx.html", {"latest_question_list": latest_question_list})

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
