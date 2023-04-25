from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
	s='<h1>hyderabad jobs information</h1>'
	return HttpResponse(s)
def keralajobsinfo(request):
	s='<h1>kerala jobs information</h1>'
	return HttpResponse(s)
def mumbaijobsinfo(request):
	s='<h1>mumbai jobs information</h1>'
	return HttpResponse(s)
def goajobsinfo(request):
	s='<h1>goa jobs information</h1>'
	return HttpResponse(s)
