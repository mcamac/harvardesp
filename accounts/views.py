from django.contrib.auth.decorators import login_required
from django.shortcuts import (
	redirect,
	render,
	render_to_response)


def do_login(request):
	if request.POST:
		pass
	else:
		pass
	return render(request, 'pages/home.html')

def do_logout(request):
	return render(request, 'pages/home.html')