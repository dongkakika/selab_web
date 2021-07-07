from django.shortcuts import render
from .models import People, Professor, Publication, Journal, Staff, Research, rp, ip
from .forms import PeopleForm, ProfessorForm, PublicationWriteForm, JournalWriteForm, StaffForm, ResearchForm, RPForm, IPForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
import os

# Create your views here.
def ip_write(request):
    if request.method == "POST":
        form = IPForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            ip = form.save(commit=False)
            ip.save()  # 내용 저장
            return redirect('ppr:professor')

    else:
        form = IPForm()
        return render(request, 'ppr/ip_write.html', {'form':form})

def rp_write(request):
    if request.method == "POST":
        form = RPForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            rp = form.save(commit=False)
            rp.save()  # 내용 저장
            return redirect('ppr:professor')

    else:
        form = RPForm()
        return render(request, 'ppr/rp_write.html', {'form':form})

@login_message_required
def research_delete(request, pk):
    research = Research.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        research.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/research')
    else:
        messages.error(request, "This access doesn't belong to you.")
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
            messages.error(request, "You don't have access")
            return redirect('/ppr/research')

def research(request):
    research_list = Research.objects.all()
    context = {
        'research_list' : research_list
    }
    return render(request, 'ppr/research.html', context)

def research_write(request):
    if request.method == "POST":
        form = ResearchForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            research = form.save(commit=False)
            if request.POST.get('img', True):
                research.img = request.FILES['img']
                messages.success(request, "등록 완료")
                research.save()
                return redirect('ppr:research')

    else:
        form = ResearchForm()
        return render(request, 'ppr/research_write.html', {'form':form})


# Publication -> journal & publications
def publication(request):

    publication_list = Publication.objects.all()
    journal_list = Journal.objects.all()

    paginator1 = Paginator(journal_list, 10)
    paginator2 = Paginator(publication_list, 10)
    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)
    page_obj2 = paginator2.get_page(page_number)

    page_range1 = page_obj1.paginator.page_range
    page_range2 = page_obj2.paginator.page_range

    context = {
        'journal_list' : page_obj1,
        'publication_list': page_obj2,
        'page_range1' : page_range1,
        'page_range2': page_range2,
    }

    return render(request, 'ppr/publication.html', context)



@login_message_required
def write_journal(request):
    if request.method == "POST":
        form = JournalWriteForm(request.POST)
        if form.is_valid():
            messages.success(request, '저장 완료')
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
            messages.success(request, '저장 완료')
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
            messages.error(request, "You don't have access")
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
            messages.error(request, "You don't have access")
            return redirect('/ppr/publication')

@login_message_required
def journal_delete(request, pk):
    journal = Journal.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        journal.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/publication')
    else:
        messages.error(request, "This post doesn't belong to you.")
        return redirect('/ppr/publication')

@login_message_required
def publication_delete(request, pk):
    publication = Publication.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        publication.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/publication')
    else:
        messages.error(request, "This post doesn't belong to you.")
        return redirect('/ppr/publication')

# members <=> People
def members(request):
    people_all = People.objects.all()
    staff_all = Staff.objects.all()
    context = {
        'people_all' : people_all,
        'staff_all' : staff_all,
    }
    return render(request, 'ppr/members.html', context)

@login_message_required
def add_member(request):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            people = form.save(commit=False)
            if request.POST.get('img_upload', True):
                people.img_upload = request.FILES['img_upload']
                messages.success(request, "등록 완료")
                people.save()
                return redirect('ppr:members')

    else:
        form = PeopleForm()
        return render(request, 'ppr/add_member.html', {'form':form})

@login_message_required
def add_other_staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            staff = form.save(commit=False)
            if request.POST.get('img_upload', True):
                staff.img_upload = request.FILES['img_upload']
                messages.success(request, "등록 완료")
                staff.save()
                return redirect('ppr:members')

    else:
        form = StaffForm()
        return render(request, 'ppr/add_other_staff.html', {'form':form})

@login_message_required
def member_modify(request, pk):
    people_current = get_object_or_404(People, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = PeopleForm(request.POST, instance=people_current)
            if form.is_valid():
                people = form.save(commit=False)
                # ** 수정할 때도 사진은 따로 변경해줘야 함
                if request.POST.get('img_upload', True):
                    people.img_upload = request.FILES['img_upload']
                    # People.objects.get(id=pk).img_upload.delete() # 이전 사진 삭제
                    messages.success(request, "Modified well" + str())
                    people.save()
                    return redirect('ppr:members')
                #messages.success(request, str(people.img_upload))
                # 사진이 없을 때의 진행 !!
                messages.success(request, "Modified well" + str())
                people.save()
                return redirect('ppr:members')

    else:
        people = People.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = PeopleForm(instance=people)
            context = {
                'form' : form,
                'people': people,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/add_member.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/ppr/members')

@login_message_required
def staff_modify(request, pk):
    staff = get_object_or_404(Staff, pk=pk)

    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = StaffForm(request.POST, instance=staff)
            if form.is_valid():
                people = form.save(commit=False)
                people.save()
                messages.success(request, 'Modified well')
                return redirect('/ppr/members')
    else:
        staff = Staff.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = StaffForm(instance=staff)
            context = {
                'form' : form,
                'staff': staff,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'ppr/add_member.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/ppr/members')

@login_message_required
def member_delete(request, pk):
    people = People.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        people.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/members')
    else:
        messages.error(request, "This access doesn't belong to you.")
        return redirect('/ppr/members')

@login_message_required
def staff_delete(request, pk):
    staff = Staff.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        staff.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/ppr/members')
    else:
        messages.error(request, "This access doesn't belong to you.")
        return redirect('/ppr/members')

# People -> Professor (independent db_table)
def professor(request):
    professor = Professor.objects.all()
    publication_list = Publication.objects.all()
    journal_list = Journal.objects.all()
    rp_list = rp.objects.all()
    ip_list = ip.objects.all()

    paginator1 = Paginator(journal_list, 10)
    paginator2 = Paginator(publication_list, 10)
    paginator3 = Paginator(rp_list, 10)
    paginator4 = Paginator(ip_list, 10)
    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)
    page_obj2 = paginator2.get_page(page_number)
    page_obj3 = paginator3.get_page(page_number)
    page_obj4 = paginator4.get_page(page_number)

    page_range1 = page_obj1.paginator.page_range
    page_range2 = page_obj2.paginator.page_range
    page_range3 = page_obj3.paginator.page_range
    page_range4 = page_obj4.paginator.page_range

    context = {
        'professor': professor,
        'journal_list': page_obj1,
        'publication_list': page_obj2,
        'rp_list': page_obj3,
        'ip_list': page_obj4,
        'page_range1': page_range1,
        'page_range2': page_range2,
        'page_range3': page_range3,
        'page_range4': page_range4,
    }

    return render(request, 'ppr/professor.html', context)

@login_message_required
def modifyProfessor(request):

    # 데이터 불러오기 or 첫 시작 예외처리
    try:
        content_first = get_object_or_404(Professor, pk=1)
    except:
        p = Professor(content='modify 버튼을 통해 내용을 작성해주세요')
        p.save()
        content_first = get_object_or_404(Professor, pk=1)

    if request.method == "POST":
        # 작성자 검사, 관리자 검사 --> 둘만 수정 가능
        if (request.user.level == '0'):
            # 기존의 제목과 내용 등 값들을 그대로 넘겨주기 위해 instance=notice(객체)로 넘김
            form = ProfessorForm(request.POST, instance=content_first)
            if form.is_valid():
                content_first = form.save(commit=False)
                content_first.save()
                messages.success(request, "Modified well.")
                return redirect('/ppr/professor')
    else:
        content_first = Professor.objects.get(id=1)
        if request.user.level == '0':
            form = ProfessorForm(instance=content_first)
            # 같은 notice_write 페이지를 쓰되, 버튼 변경을 위해 아래를 구현
            context = {
                'form': form,
                'edit': 'Save',  # 버튼의 텍스트 값
            }
            return render(request, "ppr/modifyContent.html", context)
        else:
            messages.error(request, "You have no access.")
            return redirect('/ppr/professor')

    return render(request, 'ppr/modifyContent.html')

def modify_tap(request):
    return render(request, 'ppr/')

def gallery(request):
    return render(request, 'ppr/gallery.html')