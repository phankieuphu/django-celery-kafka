from django.shortcuts import render

# Create your views here.
# from .producer import KafkaProducers


class KafkaViews():
    # def __init__(self):
    # self.producer = KafkaProducers()

    def send(self, request):
        # self.producer.send('test', 'hello world')
        return render(request, 'kafka/index.html', {})
