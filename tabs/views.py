from django.shortcuts import render
from .models import activities, award, Conference
from .forms import ActivitiesForm, AwardForm, ConferenceForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404


# Create your views here.
@login_message_required
def activities_write(request):
    if request.method == "POST":
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            activities = form.save(commit=False)
            activities.save()  # 내용 저장
            return redirect('ppr:professor')

    else:
        form = ActivitiesForm()
        return render(request, 'tabs/activities_write.html', {'form':form})