from django.urls import path
from . import views_view, views_input

urlpatterns = [
	path("", views_view.ranking, name="ranking"),
	path("daily", views_view.daily, name="daily"),
	path("input", views_input.inputScr, name="inputScr"),
	path("import", views_input.importScr, name="importScr"),
]

