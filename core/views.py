from django.contrib.auth.decorators import login_required
from django.shortcuts import (
	redirect,
	render,
	render_to_response)


def show_home(request):
	return render(request, 'pages/home.html')

def show_faq(request):
	return render(request, 'pages/faq.html')

def show_about(request):
	return render(request, 'pages/about.html')