from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from django.core.urlresolvers import reverse_lazy


class Home(ListView):
	model = Car

class CarDetail(DetailView):
	model = Car

class CarCreation(CreateView):
	model = Car
	success_url = reverse_lazy('list')
	fields = ['modelo','propietario','issue','foto']

class CarUpdate(UpdateView):
	model = Car
	success_url = reverse_lazy('list')
	fields = ['issue','status','foto']

class CarDelete(DeleteView):
	model = Car
	success_url = reverse_lazy('list')



