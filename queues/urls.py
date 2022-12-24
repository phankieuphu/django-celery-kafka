from django.urls import path
from .views import QueuViews
urlpatterns = [
    path('', QueuViews.send),
]
