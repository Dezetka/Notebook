from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('authorized/', views.AuthorizedViews.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
]
