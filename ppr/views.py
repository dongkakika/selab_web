from django.shortcuts import render
from .models import International_Journal, Domestic_Journal, Research
from tabs.models import ip, rp, activities, award, Conference, Etc
from .forms import InternationalJournalWriteForm, DomesticJournalWriteForm, ResearchForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
import os
from django.http import HttpResponse

@login_message_required
def research_delete(request, pk):
    research = Research.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        research.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/research')
    else:
        messages.error(request, "This access does not belong to you.")
        return redirect('/ppr/research')

@login_message_required
def research_modify(request, pk):
    research_current = get_object_or_404(Research, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = ResearchForm(request.POST, instance=research_current)
            if form.is_valid():
                research = form.save(commit=False)
                # ** 수정할 때도 사진은 따로 변경해줘야 함
                if request.POST.get('img', True):
                    research.img = request.FILES['img']
                    # People.objects.get(id=pk).img_upload.delete() # 이전 사진 삭제
                messages.success(request, "Modified well")
                research.save()
                return redirect('ppr:research')

    else:
        research = Research.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = ResearchForm(instance=research)
            context = {
                'form' : form,
                'research': research,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/research_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/research')

def research(request):
    research_list = Research.objects.all().order_by('-number')
    context = {
        'research_list' : research_list,
        'selected': "Research_Area",
    }
    return render(request, 'ppr/research.html', context)

@login_message_required
def research_write(request):
    if request.method == "POST":
        form = ResearchForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            research = form.save(commit=False)
            if request.POST.get('img', True):
                research.img = request.FILES['img']
            messages.success(request, "Uploaded successfully")
            research.save()
            return redirect('ppr:research')
        else:
            messages.success(request, "error")
            return redirect('ppr:research')

    else:
        form = ResearchForm()
        return render(request, 'ppr/research_write.html', {'form':form})


# Publication -> journal & publications
def publication(request):
    international_list = International_Journal.objects.all().order_by('-issued_date')
    domestic_list = Domestic_Journal.objects.all().order_by('-issued_date')
    rp_list = rp.objects.all().order_by('-period')
    ip_list = ip.objects.all().order_by('-date')
    activities_list = activities.objects.all().order_by('-announced_date')
    award_list = award.objects.all().order_by('-date')
    conference_list = Conference.objects.all().order_by('-period')
    etc_list = Etc.objects.all().order_by('-date')

    paginator1 = Paginator(international_list, 10)
    paginator2 = Paginator(domestic_list, 10)
    paginator3 = Paginator(rp_list, 10)
    paginator4 = Paginator(ip_list, 10)
    paginator5 = Paginator(activities_list, 10)
    paginator6 = Paginator(award_list, 10)
    paginator7 = Paginator(conference_list, 10)
    paginator8 = Paginator(etc_list, 10)

    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)
    page_obj2 = paginator2.get_page(page_number)
    page_obj3 = paginator3.get_page(page_number)
    page_obj4 = paginator4.get_page(page_number)
    page_obj5 = paginator5.get_page(page_number)
    page_obj6 = paginator6.get_page(page_number)
    page_obj7 = paginator7.get_page(page_number)
    page_obj8 = paginator8.get_page(page_number)

    page_range1 = page_obj1.paginator.page_range
    page_range2 = page_obj2.paginator.page_range
    page_range3 = page_obj3.paginator.page_range
    page_range4 = page_obj4.paginator.page_range
    page_range5 = page_obj5.paginator.page_range
    page_range6 = page_obj6.paginator.page_range
    page_range7 = page_obj7.paginator.page_range
    page_range8 = page_obj8.paginator.page_range

    context = {
        'international_list': page_obj1,
        'domestic_list': page_obj2,
        'rp_list': page_obj3,
        'ip_list': page_obj4,
        'activities_list': page_obj5,
        'award_list': page_obj6,
        'conference_list': page_obj7,
        'etc_list': page_obj8,

        'page_range1': page_range1,
        'page_range2': page_range2,
        'page_range3': page_range3,
        'page_range4': page_range4,
        'page_range5': page_range5,
        'page_range6': page_range6,
        'page_range7': page_range7,
        'page_range8': page_range8,
        'selected': "Academic_Activity",
    }

    if request.method == 'GET':
        q = request.GET['q']
        context['q'] = q
        return render(request, 'ppr/publication.html', context)

    return render(request, 'ppr/publication.html', context)

@login_message_required
def write_international_journal(request):
    if request.method == "POST":
        #messages.success(request, '돼?')
        form = InternationalJournalWriteForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Saved')
            journal = form.save(commit = False) # 커밋 --> False
            journal.save() # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        form = InternationalJournalWriteForm()

    return render(request, "ppr/journal_write.html", {'form': form})

@login_message_required
def write_domestic_journal(request):
    if request.method == "POST":
        form = DomesticJournalWriteForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Saved')
            publication = form.save(commit = False) # 커밋 --> False
            publication.save() # 내용 저장
            q = request.GET['q']
            return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        form = DomesticJournalWriteForm()

    return render(request, "ppr/journal_write.html", {'form': form})

@login_message_required
def international_journal_detail_view(request, pk):
    journal = get_object_or_404(International_Journal, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = InternationalJournalWriteForm(request.POST, instance=journal)
            if form.is_valid():
                journal = form.save(commit=False)
                journal.save()
                messages.success(request, 'Modified well')
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        journal = International_Journal.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = InternationalJournalWriteForm(instance=journal)
            context = {
                'form' : form,
                'journal': journal,
                'edit' : 'just for check',
                'edit1': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/journal_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def domestic_journal_detail_view(request, pk):
    journal = get_object_or_404(Domestic_Journal, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = DomesticJournalWriteForm(request.POST, instance=journal)
            if form.is_valid():
                journal = form.save(commit=False)
                journal.save()
                messages.success(request, 'Modified well')
                q = request.GET['q']
                return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        journal = Domestic_Journal.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = DomesticJournalWriteForm(instance=journal)
            context = {
                'form' : form,
                'journal': journal,
                'edit': 'just for check',
                'edit2': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/journal_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def international_journal_delete(request, pk):
    journal = International_Journal.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        journal.delete()
        messages.success(request, "Deleted successfully.")
        q = request.GET['q']
        return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        messages.error(request, "This post does not belong to you.")
        return redirect('/ppr/publication')

@login_message_required
def domestic_journal_delete(request, pk):
    domestic_journal = Domestic_Journal.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        domestic_journal.delete()
        messages.success(request, "Deleted successfully.")
        q = request.GET['q']
        return redirect('/ppr/publication/?q=' + q + "&page=1")
    else:
        messages.error(request, "This post does not belong to you.")
        return redirect('/ppr/publication')



