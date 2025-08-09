from django.urls import path

from . import views

app_name ="polls"

urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),  #localhost:8000/polls/
    # ex: specifics/polls/5/
    # the 'name' value as called by the {% url %} template tag on index.html template
    # added the word 'specifics'
    path("specifics/<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("specifics/<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("specifics/<int:question_id>/vote/", views.vote, name="vote"),
]