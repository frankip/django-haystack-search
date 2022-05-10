from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
# Create your views here.

class IndexView(ListView):
    def get(self, request):
        msg = 'Welcome to the Shit Show'
        ctx = {
            "message":msg
        }
        return render(request, 'index.html', ctx)
        # return HttpResponse(msg)P 