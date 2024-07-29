from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, render , redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import register_new_case
from .models import case
from .models import lawyer_type
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)

def checktype(request):
    return request.user.email.endswith('@nyayadhwani.com')

def client_dashboard(request):
    user=request.user
    total=case.objects.filter(client_id=user).count()
    on=case.objects.filter(client_id=user,Active="Yes").count()
    won=case.objects.filter(client_id=user,status="won").count()
    loss=case.objects.filter(client_id=user,status="lost").count()

    return render(request,'dashboard/client_dashboard.html',{'on':on,'total':total,'won': won,'loss':loss})
def lawyer_dashboard(request):
        user=request.user
        total=case.objects.filter(Lawyer_id=user).count()
        on=case.objects.filter(Lawyer_id=user,Active="Yes").count()
        won=case.objects.filter(Lawyer_id=user,status="won").count()
        loss=case.objects.filter(Lawyer_id=user,status="lost").count()
        return render(request,'dashboard/lawyer_dashboard.html',{'on':on,'total':total,'won': won,'loss':loss})

@login_required
def lawyers(request):
    if checktype(request):
        return lawyer_dashboard(request)
    else:
        raise PermissionDenied 
@login_required
def clients(request):
    if not checktype(request):
        return client_dashboard(request)
    else:
        raise PermissionDenied
def allocate_lawyer(type):
    matching_lawyers=lawyer_type.objects.filter(type_of_lawyer=type).values('lawyer_id').first()
    lawyer=matching_lawyers
    return lawyer

def reg(request):
    form = register_new_case(request.POST,request.FILES)
    if form.is_valid():
        print("yes")
        form.save()
        use=form.save()
        desc=form.cleaned_data.get('Descriptions')
        username=request.user.username
        toc=form.cleaned_data.get('type_of_case')
        proof=form.cleaned_data.get('proofs')
        law=allocate_lawyer(toc)

    else:
        print("no")
    return render(request,'dashboard/reg.html',{'form': form})

def total_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user)
    return render(request,'dashboard/client_case_list.html',{'object_list':total})
def active_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user,Active="Yes")
    return render(request,'dashboard/client_case_list.html',{'object_list':total})
def won_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user,status="won")
    return render(request,'dashboard/client_case_list.html',{'object_list':total})
def loss_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user,status="lost")
    return render(request,'dashboard/client_case_list.html',{'object_list':total})