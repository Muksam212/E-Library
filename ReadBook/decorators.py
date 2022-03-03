#decorator gives permission
#decorator is very very important for giving permission
from .models import UserInfo
from django.http import HttpResponse

def author_only(func):
	def wrapper(request, *args, **kwargs):
		if UserInfo.objects.filter(pk = request.user.id, user_type = "Author").exists():
			return func(request, *args, **kwargs)
		else:
			return HttpResponse("You have no permission to access this, Please sign up as Author")

	return wrapper
