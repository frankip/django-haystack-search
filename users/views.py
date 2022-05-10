from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
# Create your views here.

import init_db

# from .. import fetch_data_from_sql

class IndexView(ListView):
    def get(self, request):
        msg = 'Welcome to the Shit Show'
        
        users = init_db.fetch_data_from_sql()
        
        ctx = {
            "message":msg,
            "users": users
        }
        return render(request, 'index.html', ctx)
        # return HttpResponse(msg)P 