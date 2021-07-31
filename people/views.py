from django.shortcuts import render
from .models import People, Professor, Staff
from .forms import PeopleForm, ProfessorForm, StaffForm
from ppr.models import Publication, Journal
from tabs.models import ip, rp, activities, award, Conference
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404

# Create your views here.
# members <=> People
def members(request):
    people_all = People.objects.all()
    staff_all = Staff.objects.all()
    context = {
        'people_all' : people_all,
        'staff_all' : staff_all,
    }
    return render(request, 'people/members.html', context)

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
                return redirect('people:members')

    else:
        form = PeopleForm()
        return render(request, 'people/add_member.html', {'form':form})

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
                return redirect('people:members')

    else:
        form = StaffForm()
        return render(request, 'people/add_other_staff.html', {'form':form})

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
                    return redirect('people:members')
                #messages.success(request, str(people.img_upload))
                # 사진이 없을 때의 진행 !!
                messages.success(request, "Modified well" + str())
                people.save()
                return redirect('people:members')

    else:
        people = People.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = PeopleForm(instance=people)
            context = {
                'form' : form,
                'people': people,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'people/add_member.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/people/members')

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
                return redirect('/people/members')
    else:
        staff = Staff.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = StaffForm(instance=staff)
            context = {
                'form' : form,
                'staff': staff,
                'edit': 'Modify', # 버튼의 텍스트 값
            }
            return render(request, 'people/add_member.html', context)
        else:
            messages.error(request, "You don't have access")
            return redirect('/people/members')

@login_message_required
def member_delete(request, pk):
    people = People.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        people.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/people/members')
    else:
        messages.error(request, "This access doesn't belong to you.")
        return redirect('/people/members')

@login_message_required
def staff_delete(request, pk):
    staff = Staff.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0':
        staff.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/people/members')
    else:
        messages.error(request, "This access doesn't belong to you.")
        return redirect('/people/members')

# People -> Professor (independent db_table)
def professor(request):
    professor = Professor.objects.all()
    publication_list = Publication.objects.all().order_by('-published_date')
    journal_list = Journal.objects.all().order_by('issued_date')
    rp_list = rp.objects.all().order_by('-period')
    ip_list = ip.objects.all().order_by('-date')
    activities_list = activities.objects.all().order_by('-announced_date')

    paginator1 = Paginator(journal_list, 10)
    paginator2 = Paginator(publication_list, 10)
    paginator3 = Paginator(rp_list, 10)
    paginator4 = Paginator(ip_list, 10)
    paginator5 = Paginator(activities_list, 10)
    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)
    page_obj2 = paginator2.get_page(page_number)
    page_obj3 = paginator3.get_page(page_number)
    page_obj4 = paginator4.get_page(page_number)
    page_obj5 = paginator5.get_page(page_number)

    page_range1 = page_obj1.paginator.page_range
    page_range2 = page_obj2.paginator.page_range
    page_range3 = page_obj3.paginator.page_range
    page_range4 = page_obj4.paginator.page_range
    page_range5 = page_obj5.paginator.page_range

    context = {
        'professor': professor,
        'journal_list': page_obj1,
        'publication_list': page_obj2,
        'rp_list': page_obj3,
        'ip_list': page_obj4,
        'activities_list': page_obj5,

        'page_range1': page_range1,
        'page_range2': page_range2,
        'page_range3': page_range3,
        'page_range4': page_range4,
        'page_range5': page_range5,
    }

    return render(request, 'people/professor.html', context)

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
                return redirect('/people/professor')
    else:
        content_first = Professor.objects.get(id=1)
        if request.user.level == '0':
            form = ProfessorForm(instance=content_first)
            # 같은 notice_write 페이지를 쓰되, 버튼 변경을 위해 아래를 구현
            context = {
                'form': form,
                'edit': 'Save',  # 버튼의 텍스트 값
            }
            return render(request, "people/modifyContent.html", context)
        else:
            messages.error(request, "You have no access.")
            return redirect('/people/professor')

    return render(request, 'people/modifyContent.html')