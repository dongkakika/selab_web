from django.shortcuts import render
from .models import Publication, Journal, Research
from ppr.models import Publication, Journal
from tabs.models import ip, rp, activities, award, Conference
from .forms import PublicationWriteForm, JournalWriteForm, ResearchForm
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
    research_list = Research.objects.all()
    context = {
        'research_list' : research_list
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
    journal_list = Journal.objects.all().order_by('-issued_date')
    publication_list = Publication.objects.all().order_by('-published_date')
    rp_list = rp.objects.all().order_by('-period')
    ip_list = ip.objects.all().order_by('-date')
    activities_list = activities.objects.all().order_by('-announced_date')
    award_list = award.objects.all().order_by('-date')
    conference_list = Conference.objects.all().order_by('-period')

    paginator1 = Paginator(journal_list, 10)
    paginator2 = Paginator(publication_list, 10)
    paginator3 = Paginator(rp_list, 10)
    paginator4 = Paginator(ip_list, 10)
    paginator5 = Paginator(activities_list, 10)
    paginator6 = Paginator(award_list, 10)
    paginator7 = Paginator(conference_list, 10)
    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)
    page_obj2 = paginator2.get_page(page_number)
    page_obj3 = paginator3.get_page(page_number)
    page_obj4 = paginator4.get_page(page_number)
    page_obj5 = paginator5.get_page(page_number)
    page_obj6 = paginator6.get_page(page_number)
    page_obj7 = paginator7.get_page(page_number)

    page_range1 = page_obj1.paginator.page_range
    page_range2 = page_obj2.paginator.page_range
    page_range3 = page_obj3.paginator.page_range
    page_range4 = page_obj4.paginator.page_range
    page_range5 = page_obj5.paginator.page_range
    page_range6 = page_obj6.paginator.page_range
    page_range7 = page_obj7.paginator.page_range

    context = {
        'journal_list': page_obj1,
        'publication_list': page_obj2,
        'rp_list': page_obj3,
        'ip_list': page_obj4,
        'activities_list': page_obj5,
        'award_list': page_obj6,
        'conference_list': page_obj7,

        'page_range1': page_range1,
        'page_range2': page_range2,
        'page_range3': page_range3,
        'page_range4': page_range4,
        'page_range5': page_range5,
        'page_range6': page_range6,
        'page_range7': page_range7
    }

    return render(request, 'ppr/publication.html', context)



@login_message_required
def write_journal(request):
    if request.method == "POST":
        #messages.success(request, '돼?')
        form = JournalWriteForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Saved')
            journal = form.save(commit = False) # 커밋 --> False
            journal.save() # 내용 저장
            return redirect('ppr:publication')
    else:
        form = JournalWriteForm()

    return render(request, "ppr/journal_write.html", {'form': form})

@login_message_required
def write_publication(request):
    if request.method == "POST":
        form = PublicationWriteForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Saved')
            publication = form.save(commit = False) # 커밋 --> False
            publication.save() # 내용 저장
            return redirect('ppr:publication')
    else:
        form = PublicationWriteForm()

    return render(request, "ppr/publication_write.html", {'form': form})

@login_message_required
def journal_detail_view(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = JournalWriteForm(request.POST, instance=journal)
            if form.is_valid():
                journal = form.save(commit=False)
                journal.save()
                messages.success(request, 'Modified well')
                return redirect('/ppr/publication')
    else:
        journal = Journal.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = JournalWriteForm(instance=journal)
            context = {
                'form' : form,
                'journal': journal,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/journal_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def publication_detail_view(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = PublicationWriteForm(request.POST, instance=publication)
            if form.is_valid():
                publication = form.save(commit=False)
                publication.save()
                messages.success(request, 'Modified well')
                return redirect('/ppr/publication')
    else:
        publication = Publication.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = PublicationWriteForm(instance=publication)
            context = {
                'form' : form,
                'publication': publication,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/publication_write.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('/ppr/publication')

@login_message_required
def journal_delete(request, pk):
    journal = Journal.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        journal.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/publication')
    else:
        messages.error(request, "This post does not belong to you.")
        return redirect('/ppr/publication')

@login_message_required
def publication_delete(request, pk):
    publication = Publication.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        publication.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/publication')
    else:
        messages.error(request, "This post does not belong to you.")
        return redirect('/ppr/publication')



