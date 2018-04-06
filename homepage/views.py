from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="users/login")

def homepage(request):
    context = {'user': request.user}
    return render(request, 'homepage/homepage.html', context)

def workouts(request, userID):
    user = User.objects.get(id=userID)
    return render(request, 'homepage/workouts.html')

def public_logs(request):

    users = User.objects.all()
    context = { 'users': users }
    print(context)

    return render(request, 'homepage/public_logs.html', context)

def public_log(request, userID):
    user = User.objects.get(id=userID)
    request.user = user
    print(request.user)
    return render(request, 'homepage/workouts.html')
