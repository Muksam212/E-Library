
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ReadBook" #custom url which is very important

urlpatterns = [
	path('', views.loadBook, name='premiumbook'),
	path('addbook/',views.addBook, name='addbook'),
	path('description/<int:bid>/', views.bookDescription, name='description'),
	path('delete/<int:bid>/', views.deleteBook, name='deletebook')
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)