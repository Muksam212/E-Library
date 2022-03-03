from django.shortcuts import render, redirect
from .models import Book
from .decorators import author_only
from django.contrib.auth.decorators import login_required
# Create your views here.
def loadBook(request):
	books = Book.objects.all()
	context = {'books':books}
	return render(request,'Readbook/book.html',context)

@login_required(login_url='/login/')
@author_only
def addBook(request):
	name = ''
	price = ''
	btype = ''
	cover = ''
	pdf = ''
	description =''
	category = ''
	userid = ''
	if request.method == "POST":

		try:
			name = request.POST['name'].strip() #removes white space
			btype = request.POST['btype'].strip() #remove white space
			description = request.POST['description']
			category = request.POST['category']
			cover = request.FILES.get('image', None)
			pdf = request.FILES.get('file')
			userid = request.user.id


			if btype != 'Free':
				price = int(request.POST['price'])
			else:
				price = 0

			Book.objects.create(book_name = name, book_price = price, book_type = btype,
				book_category = category, book_cover = cover, book_description = description,
				book_file = pdf, uploaded_by_id = userid)
			return redirect("Readbook:premiumbook")

		except Exception as e:
			print("Error:"+str(e))


	return render(request,'Readbook/AddBook.html', context ={
			'bookname':name,
			'bookprice':price,
			'category':category,
			'description':description

		})


def bookDescription(request, bid):
	book = None
	owner = False
	loggedin = True if request.user.is_authenticated else False

	if Book.objects.filter(id = bid).exists():
		try:
			book = Book.objects.get(id=bid)
			if loggedin:
				owner = True if Book.objects.get(pk=bid).uploaded_by_id == request.user.id else False
		except Exception as e:
			print(str(e))

	else:
		return redirect('ReadBook:premiumbook')

	return render(request,'Readbook/BookDescription.html',context={
			'book' : book,
			'loggedin' : loggedin,
			'owner' : owner

		})

@login_required(login_url='/login/')
@author_only
def deleteBook(request, bid):
	book = None
	if Book.objects.filter(id = bid).exists():
		book = Book.objects.get(id = bid)
		book.delete()
	return redirect('ReadBook:premiumbook')