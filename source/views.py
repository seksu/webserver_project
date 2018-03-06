# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , redirect

from django.http import HttpResponse

from django.template import loader

from django.core.files.storage import FileSystemStorage

from django.conf import settings

from account.models import Account
from rest_framework import viewsets

# Create your views here.

print("test pass")

def index(request):
	print("test pass 2")
	print('request : '+ str(request))
	if request.method == 'POST' and request.FILES['myfile']:

		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		print('uploaded_file_url : '+str(uploaded_file_url))
		return render(request, 'search.html', {'uploaded_file_url': uploaded_file_url})
	#if(shirtColor):
	#	print("shirtColor : " + str(shirtColor))
	return render(request, 'search.html')
def sek(request):
	return render(request,'sek.html')

def template(request):
	#templete = loader.get_template('index.html')
	return render(request,'index.html')

def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Account.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer