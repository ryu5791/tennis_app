from django.urls import path
from . import views_view

urlpatterns = [
	path("", views_view.ranking, name="ranking"),
	path("daily", views_view.daily, name="daily"),
]

