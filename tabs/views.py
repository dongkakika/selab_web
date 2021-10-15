from django.shortcuts import render
from .models import activities, award, Conference, ip, rp, Etc
from .forms import IPForm, RPForm, ActivitiesForm, AwardForm, ConferenceForm, EtcWriteForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# Create your views here.
@login_message_required
def ip_write(request):
    if request.method == "POST":
        form = IPForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            ip = form.save(commit=False)
            ip.save()  # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")

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
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
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
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def rp_write(request):
    if request.method == "POST":
        form = RPForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            rp = form.save(commit=False)
            rp.save()  # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")

    else:
        form = RPForm()
        return render(request, 'tabs/rp_write.html', {'form':form})

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
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
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
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def activities_write(request):
    if request.method == "POST":
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            activities = form.save(commit=False)
            activities.save()  # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")

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
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        Activities = activities.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = ActivitiesForm(instance=Activities)
            context = {
                'form' : form,
                'activities': Activities,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/activities_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def award_write(request):
    if request.method == "POST":
        form = AwardForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            award = form.save(commit=False)
            award.save()  # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")

    else:
        form = AwardForm()
        return render(request, 'tabs/award_write.html', {'form':form})

@login_message_required
def award_modify(request, pk):
    Award = get_object_or_404(award, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = AwardForm(request.POST, instance=Award)
            if form.is_valid():
                award_form = form.save(commit=False)
                award_form.save()
                messages.success(request, 'Modified well')
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        Award = award.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = AwardForm(instance=Award)
            context = {
                'form' : form,
                'award': Award,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/award_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def conference_write(request):
    if request.method == "POST":
        form = ConferenceForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            conference = form.save(commit=False)
            conference.save()  # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")

    else:
        form = ConferenceForm()
        return render(request, 'tabs/conference_write.html', {'form':form})

@login_message_required
def conference_modify(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = ConferenceForm(request.POST, instance=conference)
            if form.is_valid():
                conference_form = form.save(commit=False)
                conference_form.save()
                messages.success(request, 'Modified well')
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        conference = Conference.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = ConferenceForm(instance=conference)
            context = {
                'form' : form,
                'conference': conference,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/conference_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def etc_write(request):
    if request.method == "POST":
        form = EtcWriteForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Saved')
            etc = form.save(commit = False) # 커밋 --> False
            etc.save() # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        form = EtcWriteForm()

    return render(request, "tabs/etc_write.html", {'form': form})

@login_message_required
def etc_modify(request, pk):
    etc = get_object_or_404(Etc, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = EtcWriteForm(request.POST, instance=etc)
            if form.is_valid():
                etc = form.save(commit=False)
                etc.save()
                messages.success(request, 'Modified well')
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        etc = Etc.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = EtcWriteForm(instance=etc)
            context = {
                'form' : form,
                'etc': etc,
                'edit' : 'just for check',
                'edit1': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'tabs/etc_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')



class award_delete(DeleteView):
    model = award
    success_url = str('/ppr/publication') + '?q=4&?page=1'

    def get(self, request, *args, **kwargs):

        return self.post(request, *args, **kwargs)

class activities_delete(DeleteView):
    model = activities
    success_url = str('/ppr/publication') + '?q=7&?page=1'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ip_delete(DeleteView):
    model = ip
    success_url = str('/ppr/publication') + '?q=6&?page=1'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class rp_delete(DeleteView):
    model = rp
    success_url = str('/ppr/publication') + '?q=5&?page=1'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class conference_delete(DeleteView):
    model = Conference
    success_url = str('/ppr/publication') + '?q=3&?page=1'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class etc_delete(DeleteView):
    model = Etc
    success_url = str('/ppr/publication') + '?q=8&?page=1'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)