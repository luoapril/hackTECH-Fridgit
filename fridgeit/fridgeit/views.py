from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from fridgeit.models import User
from pinterest.models.model import Pinterest, User
import pinterest.search as search

CLIENT_ID = "1435790"
CLIENT_SECRET = "8c8eab09fe710377c9e879872855109c9f349195"
Pinterest.configure_client(CLIENT_ID, CLIENT_SECRET)

from django.core.urlresolvers import reverse
from fridgeit.models import User

def home(request):
	return render(request, 'landing.html')

def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

def userlogin(request):
	if request.method =="POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		print username
		user = authenticate(username = username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				print "logged {} in ".format(user.username)
				return HttpResponseRedirect('/index')
	return HttpResponseRedirect('/')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def index(request):
	return render(request, 'index.html')

def signup(request):
	return render(request, 'signup.html')

def get_recipe(request):
	#get ingredients
	ingredients = ['chocolate', 'strawberry', 'cream']
	#ingredients = ['avocado', 'egg', 'milk', 'chocolate', 'strawberry']
	size = len(ingredients)
	
	#convert ingredients to string query
	query = ""
	for i in range(0, size):
		query = query + ingredients[i] + " "

	#prepare search results	
	results = search.pins(query="fudge", rich_type="recipe", rich_query=query, restrict="food_drink", boost="quality")
	pin_name = []
	pin_url = []

	print(len(results))

	if len(results)>0 :
		#convert results to be used in recipes.html
		for x in range (0, len(results)):
			pin_name.append(results[x].description)
			pin_url.append(results[x].image_medium_url)

		print(pin_url)
		return render(request, 'recipes.html', {'names': pin_name, 'urls': pin_url, 'quartile': range(0, len(results)), 'empty': False})
	else :
		return render(request, 'recipes.html', {'empty': True})











