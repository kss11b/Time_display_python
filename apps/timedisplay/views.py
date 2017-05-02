from django.shortcuts import render
import time
from datetime import datetime
def index(request):
    print datetime.now()
    context= {
    "datetime":datetime.now()


    }
    return render(request, 'timedisplay/index.html', context)
# Create your views here.
