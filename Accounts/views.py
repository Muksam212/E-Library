from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from ReadBook.models import UserInfo
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_user(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			username = request.POST['username']
			email = request.POST['email']
			user_type = request.POST['user_type']
			password1 = request.POST['password1']
			password2 = request.POST['password2']

			if password1 == password2:
				if User.objects.filter(username = username).exists():
					messages.info(request,'Username is taken. Choose Another')
					return redirect('Accounts:register_user')

				elif User.objects.filter(email = email).exists():
					messages.info(request,"Email is taken. Take another email")
					return redirect('Accounts:register_user')

				else:
					user = User.objects.create_user(username = username, password = password1,first_name = first_name, 
						last_name = last_name, email = email)
					user.save()
					UserInfo.objects.create(id = user.id, user_type = user_type, 
						users_id = user.id)
					return redirect('Accounts:login_user')
				#pretty Jharna123
				#muksam ethicalhacker
			else:
				messages.info(request,'Password does not matched')
				return redirect('Accounts:register_user')
	return render(request,'Accounts/register.html')


def login_user(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']

			user = auth.authenticate(username = username, password = password)
			if user is not None:
				auth.login(request, user)
				return redirect('/')
			else:
				messages.info(request,f'Invalid Credential')
				return redirect("Accounts:login_user")#<app_name>:<url> custom url
		else:
			return render(request,'Accounts/login.html')
	else:
		return HttpResponse("You are not permitted to view this page")

def logout_user(request):
	auth.logout(request)
	return redirect('Accounts:login_user')