from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Complaint
from .forms import RegistrationForm, ComplaintForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Account created successfully')
            login(request,user)#this automatically login the registered user

            return redirect('home')

    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    complaint = Complaint.objects.filter(user=request.user)
    #taking and storing q value from the webpage and to query
    query=request.GET.get('q')
    if query:#if search has anything
        complaint=Complaint.objects.filter(user=request.user,title__icontains=query)#check whether the title contains the query that is search word icontains for case insensitivity
    else:
        complaint = Complaint.objects.filter(user=request.user)#show all complaints of the logined users
    if request.method== 'POST':
        form =ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            complaints=form.save(commit=False)
            complaints.user=request.user
            complaints.save()
            messages.success(request, 'Complaint added successfully')
            return redirect('home')
    else:
        form = ComplaintForm()
    return render(request, 'home.html', {'form': form,"complaint":complaint})

def update(request,id):
    complaint = Complaint.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint updated successfully')
            return redirect('home')
    else:
        form =ComplaintForm(instance=complaint)
    return render(request, 'update.html', {'form': form,} )
def delete(request,id):
    complaint = Complaint.objects.get(id=id, user=request.user)
    complaint.delete()
    return redirect('home')