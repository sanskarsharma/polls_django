from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # path("", views.home, name="home"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results", views.results, name="results"),
    # path("<int:question_id>/vote", views.vote, name="vote")
    # urls for generic views below
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote", views.vote, name="vote")
]