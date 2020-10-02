from django.urls import path
from .views import HomePageView
from .views import homePageView




urlpatterns = [
    #path('', HomePageView.as_view(), name="home"), # the class based view
    path('', homePageView, name="home") # The function based view


]
