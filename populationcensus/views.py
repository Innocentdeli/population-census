from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Populationcensus
from django.urls import reverse
from django.db.models import Q
from .forms import censusRegistrationAndUpdateForm


def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())


def index(request):
    mypopulationcensus = Populationcensus.objects.all()
    gradeA = mypopulationcensus.filter(Q(age__gte = 30) & Q(gender__exact = "m"))
    gradeB = mypopulationcensus.filter(Q(age__gte = 30) & Q(gender__exact = "f"))
    gradeC = mypopulationcensus.filter(Q(age__gte = 18) & Q(age__lte = 29) & Q(gender__exact = "m"))
    gradeD = mypopulationcensus.filter(Q(age__gte = 18) & Q(age__lte = 29) & Q(gender__exact = "f"))
    gradeE = mypopulationcensus.filter(Q(age__gte = 0) & Q(age__lte = 17) & Q(gender__exact = "m"))
    gradeF = mypopulationcensus.filter(Q(age__gte = 0) & Q(age__lte = 17) & Q(gender__exact = "f"))
    template = loader.get_template('index.html')
    context = {
        'mypopulationcensus': mypopulationcensus,
        'gradeA': gradeA,
        'gradeB': gradeB,
        'gradeC': gradeC,
        'gradeD': gradeD,
        'gradeE': gradeE,
        'gradeF': gradeF
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    
    if request.method == "POST":
        form = censusRegistrationAndUpdateForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender'].lower()
            if len(gender) > 1:
              gender = gender[0]
            else:
                gender = gender
    populationcensus = Populationcensus(firstname = firstname, lastname = lastname, age = age, gender = gender)
    populationcensus.save()

    return HttpResponseRedirect(reverse('add'))

def delete(request, id):
  populationcensus = Populationcensus.objects.get(id=id)
  populationcensus.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mypopulationcensus = Populationcensus.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        'mypopulationcensus' : mypopulationcensus,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  if request.method == "POST":
        form = censusRegistrationAndUpdateForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender'].lower()
            if len(gender) > 1:
              gender = gender[0]
            else:
                gender = gender
  populationcensus = Populationcensus.objects.get(id=id)
  populationcensus.firstname = firstname
  populationcensus.lastname = lastname
  populationcensus.age = age
  populationcensus.gender = gender
  populationcensus.save()
  return HttpResponseRedirect(reverse('index'))
