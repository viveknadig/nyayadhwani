from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, render , redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import register_new_case,update_case_form
from .models import case
from .models import lawyer_type
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)
from django.core.exceptions import PermissionDenied

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
        total=case.objects.filter(lawyer=user).count()
        on=case.objects.filter(lawyer=user,Active="Yes").count()
        won=case.objects.filter(lawyer=user,status="won").count()
        loss=case.objects.filter(lawyer=user,status="lost").count()
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
    matching_lawyers_id=lawyer_type.objects.filter(type_of_lawyer=type).values('lawyer').first()
    lawyer_id=matching_lawyers_id.get('lawyer')
    return lawyer_id


# case registration
@login_required
def register_case(request):
    form = register_new_case(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        new_case=case(client_id_id=request.user.id,lawyer_id=allocate_lawyer(form.cleaned_data.get('type_of_case')),Description=form.cleaned_data.get('Descriptions'),image=form.cleaned_data.get('proofs'))
        new_case.save()
        return redirect('users:dashboard')
    else:
        form = register_new_case
    return render(request,'dashboard/register_case.html',{'form': form})

# dashboard for clients
@login_required
def total_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user)
    return render(request,'dashboard/client_case_list.html',{'object_list':total})
@login_required
def active_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user,Active="Yes")
    return render(request,'dashboard/client_case_list.html',{'object_list':total})
@login_required
def won_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user,status="won")
    return render(request,'dashboard/client_case_list.html',{'object_list':total})
@login_required
def loss_client_list(request):
    user=request.user
    total=case.objects.filter(client_id=user,status="lost")
    return render(request,'dashboard/client_case_list.html',{'object_list':total})

# dashboard for lawyers

@login_required
def total_lawyer_list(request):
    user=request.user
    total=case.objects.filter(lawyer=user)
    return render(request,'dashboard/lawyer_case_list.html',{'object_list':total})
@login_required
def active_lawyer_list(request):
    user=request.user
    total=case.objects.filter(lawyer=user,Active="Yes")
    return render(request,'dashboard/lawyer_case_list.html',{'object_list':total})
@login_required
def won_lawyer_list(request):
    user=request.user
    total=case.objects.filter(lawyer=user,status="won")
    return render(request,'dashboard/lawyer_case_list.html',{'object_list':total})
@login_required
def loss_lawyer_list(request):
    user=request.user
    total=case.objects.filter(lawyer=user,status="lost")
    return render(request,'dashboard/lawyer_case_list.html',{'object_list':total})


# generics for update and view
def case_view_permission_lawyer(request,pk):
    return case.objects.filter(lawyer = request.user,case_id = pk)
def case_view_permission_client(request,pk):
    return case.objects.filter(client_id = request.user,case_id = pk)

def case_view_check(request,pk):
    if checktype(request):
        return case_view_lawyer(request,pk)
    else:
        return case_view_client(request,pk)

@login_required    
def case_view_lawyer(request,pk):
    if case_view_permission_lawyer(request,pk):
        details=case.objects.filter(lawyer=request.user,case_id=pk)
        return render(request,'dashboard/view.html',{'details':details})
    else:
        raise PermissionDenied()
    
@login_required
def case_view_client(request,pk):
    if case_view_permission_client(request,pk):
        details=case.objects.filter(client_id=request.user,case_id=pk)
        return render(request,'dashboard/view.html',{'details':details})
    else:
        raise PermissionDenied()
@login_required
def update_case(request,pk):
    if case_view_permission_lawyer(request,pk):
        details_get=case.objects.get(case_id=pk)        
        details=update_case_form(request.POST,instance=details_get)
        if details.is_valid():
            details.save()
            return redirect('users:dashboard')
        else:
            details=update_case_form
        return render(request,'dashboard/update_case.html',{'details': details})
    else:
        raise PermissionDenied        
