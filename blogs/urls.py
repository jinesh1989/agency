from django.urls import path
from blogs import views

urlpatterns = [
    path("", views.BlogPageView.as_view(), name="blogpage"),
]
