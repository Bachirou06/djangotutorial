from django.urls import path
from . import views
#from ..mysite.urls import app_name

#from ..mysite.urls import urlpatterns
app_name = "poll"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.result, name="result"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]

