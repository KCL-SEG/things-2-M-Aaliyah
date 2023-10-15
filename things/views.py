from django.shortcuts import render

from things.models import Thing

def home(request):
    form = Thing()
    return render(request, 'home.html', {'form': form})
