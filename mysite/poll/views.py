from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from . models import Question, Choice

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

def indexx(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("poll/index.html")
    context = {"latest_question_list": latest_question_list}
    #output = ";".join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def indexs(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "poll/index.html", context)


### Use django generic view
class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "poll/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "poll/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(
            request, "poll/detail.html", {
                "question": question,
                "error_message": "You didn't select a choice"
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponse after successfully dealing
        # With POST data. This prevents data from being posted twice if
        # user hits the back button
        return HttpResponseRedirect(reverse("poll:result", args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "poll/results.html", {"question": question})



