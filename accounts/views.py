from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth 

# Create your views here.
def signup(request):
  if request.method == 'POST':
    if request.POST['password'] == request.POST['confirm']:
      try:
        user = User.objects.get(username=request.POST['username'])
        return render(request, 'accounts/signup.html', {'errors': 'Username has already been taken, sorry!'})
      except User.DoesNotExist:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['confirm'])
        auth.login(request,user) 
        return redirect('home')   
  else:
    return render(request,'accounts/signup.html')


def login(request):
  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      auth.login(request,user)
      return redirect('home')
    else:
      return render(request,'accounts/login.html',{'errors' : 'username or password is incorrect!'})
  else:
    return render(request,'accounts/login.html')




def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('home')
