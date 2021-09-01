from django.shortcuts import render
from .models import People, Professor, Staff
from .forms import PeopleForm, ProfessorForm, StaffForm
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
from main.decorators import admin_required, login_message_required
from django.shortcuts import get_object_or_404

# Create your views here.
# members <=> People
def members(request):
    alumni_all = People.objects.filter(delimiter=0)
    postDoctor_all = People.objects.filter(delimiter=1)
    phd_all = People.objects.filter(delimiter=2)
    master_all = People.objects.filter(delimiter=3)
    undergraduate_all = People.objects.filter(delimiter=4)
    context = {
        'alumni_all': alumni_all,
        'postDoctor_all': postDoctor_all,
        'phd_all': phd_all,
        'master_all': master_all,
        'undergraduate_all': undergraduate_all,
    }
    return render(request, 'people/members.html', context)

@login_message_required
def add_member(request, pk):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            people = form.save(commit=False)
            if request.POST.get('img_upload', True):
                people.img_upload = request.FILES['img_upload']
            people.delimiter = pk
            messages.success(request, "Saved")
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
            messages.success(request, "Saved")
            staff.save()
            return redirect('people:members')

    else:
        form = StaffForm()
        return render(request, 'people/add_other_staff.html', {'form':form})

@login_message_required
def member_modify(request, pk):
    people_current = get_object_or_404(People, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1' or request.user.level == '3' and request.user.username == people_current.name:
            form = PeopleForm(request.POST, instance=people_current)
            if form.is_valid():
                people = form.save(commit=False)
                # ** 수정할 때도 사진은 따로 변경해줘야 함
                if request.POST.get('img_upload', True):
                    people.img_upload = request.FILES['img_upload']
                    # People.objects.get(id=pk).img_upload.delete() # 이전 사진 삭제
                # 사진이 없을 때의 진행 !!
                messages.success(request, "Modified well")
                people.save()
                return redirect('people:members')

    else:
        people = People.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1' or request.user.level == '2' and request.user.username == people.name:
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
    staff_current = get_object_or_404(Staff, pk=pk)

    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1' or request.user.level == '3' and request.user.username == staff_current.name:
            form = StaffForm(request.POST, instance=staff_current)
            if form.is_valid():
                # when the photo's modification was detected
                if request.POST.get('img_upload', True):
                    staff_current.img_upload = request.FILES['img_upload']
                staff = form.save(commit=False)
                staff.save()
                messages.success(request, 'Modified well')
                return redirect('/people/members')
    else:
        staff = Staff.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1' or request.user.level == '3' and request.user.username == staff.name:
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

# 해당 로직으로 alumni 등록
@login_message_required
def alumni_registration(request, pk):
    if request.user.level == '0' or request.user.level == '1':
        people = People.objects.get(id=pk)
        people.delimiter = 0
        people.save()
        return redirect('/people/members/')
    else:
        messages.success(request, "you have no access.")
        return redirect('/people/members/')


@login_message_required
def member_delete(request, pk):
    people = People.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0' or request.user.level == '3' and request.user.username == people.name:
        people.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/people/members')
    else:
        messages.error(request, "This access doesn't belong to you.")
        return redirect('/people/members')

@login_message_required
def staff_delete(request, pk):
    staff = Staff.objects.get(id=pk)
    if request.user.level == '1' or request.user.level == '0' or request.user.level == '3' and request.user.username == staff.name:
        staff.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/people/members')
    else:
        messages.error(request, "This access doesn't belong to you.")
        return redirect('/people/members')

# People -> Professor (independent db_table)
def professor(request):
    professor = Professor.objects.all()
    context = {
        'professor': professor,
    }
    return render(request, 'people/professor.html', context)

@login_message_required
def modifyProfessor(request):

    # 데이터 불러오기 or 첫 시작 예외처리
    try:
        content_first = Professor.objects.first()
    except:
        p = Professor(content='Please modify using the button.')
        p.save()
        content_first = Professor.objects.first()

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
        content_first = Professor.objects.first()
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