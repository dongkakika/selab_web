from django.shortcuts import render
from .models import activities, award, Conference, ip, rp
from .forms import IPForm, RPForm, ActivitiesForm, AwardForm, ConferenceForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404


# Create your views here.
@login_message_required
def ip_write(request):
    if request.method == "POST":
        form = IPForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            ip = form.save(commit=False)
            ip.save()  # 내용 저장
            return redirect('people:professor')

    else:
        form = IPForm()
        return render(request, 'tabs/ip_write.html', {'form':form})

@login_message_required
def ip_modify(request, pk):
    IP = get_object_or_404(ip, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = IPForm(request.POST, instance=IP)
            if form.is_valid():
                IP_form = form.save(commit=False)
                IP_form.save()
                messages.success(request, 'Modified well')
                return redirect('/people/professor')
    else:
        IP = ip.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = IPForm(instance=IP)
            context = {
                'form' : form,
                'IP': IP,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/ip_write.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/people/professor')

@login_message_required
def rp_write(request):
    if request.method == "POST":
        form = RPForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            rp = form.save(commit=False)
            rp.save()  # 내용 저장
            return redirect('people:professor')

    else:
        form = RPForm()
        return render(request, 'tabs/activities_write.html', {'form':form})

@login_message_required
def rp_modify(request, pk):
    RP = get_object_or_404(rp, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = RPForm(request.POST, instance=RP)
            if form.is_valid():
                RP_form = form.save(commit=False)
                RP_form.save()
                messages.success(request, 'Modified well')
                return redirect('/people/professor')
    else:
        RP = rp.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = RPForm(instance=RP)
            context = {
                'form' : form,
                'RP': RP,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/rp_write.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/people/professor')

@login_message_required
def activities_write(request):
    if request.method == "POST":
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            activities = form.save(commit=False)
            activities.save()  # 내용 저장
            return redirect('people:professor')

    else:
        form = ActivitiesForm()
        return render(request, 'tabs/activities_write.html', {'form':form})

@login_message_required
def activities_modify(request, pk):
    Activities = get_object_or_404(activities, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = ActivitiesForm(request.POST, instance=Activities)
            if form.is_valid():
                activities_form = form.save(commit=False)
                activities_form.save()
                messages.success(request, 'Modified well')
                return redirect('/people/professor')
    else:
        Activities = activities.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = ActivitiesForm(instance=Activities)
            context = {
                'form' : form,
                'Activities': Activities,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/activities_write.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/people/professor')