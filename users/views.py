from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
# Create your views here.

class IndexView(ListView):
    def get(self, request):
        msg = '<h1>Welcome to the Shit Show </h1>'
        # return render(request, msg)
        return HttpResponse(msg)