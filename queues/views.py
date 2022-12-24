from django.shortcuts import render
from .tasks import longtime_add
import datetime
# Create your views here.
from django.http import HttpResponse


class QueuViews():
    def __init__(self):
        # self.get_response = get_response
        pass

    def send(request):
        print(datetime.datetime.now())
        longtime_add.delay(1, 2)
        print(datetime.datetime.now())
        my_dict = {'name': 'Alice', 'age': 30}
        return HttpResponse("Http request is: "+str(200))
