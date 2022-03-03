from django.urls import path
from Accounts import views
from django.conf import settings
from django.conf.urls.static import static

app_name ="Accounts" #custom url
urlpatterns = [
	path('register/', views.register_user, name='register_user'),
	path('login/', views.login_user, name='login_user'),
	path('logout/', views.logout_user, name='logout_user')
]

urlpatterns +=  static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


urlpatterns +=  static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)