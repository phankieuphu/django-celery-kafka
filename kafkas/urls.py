from .views import KafkaViews
from django.urls import path

urlpatterns = [
    path('', KafkaViews().send),
]
