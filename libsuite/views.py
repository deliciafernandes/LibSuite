from django.shortcuts import render
from .models import Book
from django.http import HttpRequest

def home(request):
	return render(request, 'libsuite/home.html')

def about(request):
	previous_page = request.META.get('HTTP_REFERER')

	return render(request, 'libsuite/about.html',{'previous_page' : previous_page})

def faq(request):

	previous_page = request.META.get('HTTP_REFERER')
	# NOTE : request.META.get('HTTP_REFERER') returns a string!
	# the return statement must pass a dict context only, and string is not one!
	# thus ERROR (if i dont put previous_page in a dictionary ) :
	# TypeError at /faq/
	# context must be a dict rather than str.
	
	return render(request, 'libsuite/faq.html', {'previous_page' : previous_page})

def allbooks(request):
	#context is a dictionary used to pass data to the template
	context={
		#here 'books': books, 'books' is  key while books is the books dummy data itself
		'books': Book.objects.all()
	}

	return render(request, 'libsuite/allbooks.html', context)