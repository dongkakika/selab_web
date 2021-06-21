from django.shortcuts import render
from .models import People
from .forms import PeopleForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def people(request):
    people_first = People.objects.get(id=1)
    context = {
        'people_first' : people_first,
    }

    return render(request, 'ppr/people.html', context)

def gallery(request):
    return render(request, 'ppr/gallery.html')

def modifyContent(request):
    people_first = People.objects.get(id=1)

    if request.method == "POST":
        # 작성자 검사, 관리자 검사 --> 둘만 수정 가능
        if (request.user.level == '0'):
            # 기존의 제목과 내용 등 값들을 그대로 넘겨주기 위해 instance=notice(객체)로 넘김
            form = PeopleForm(request.POST, instance=people_first)
            if form.is_valid():
                people_first = form.save(commit=False)
                people_first.save()
                messages.success(request, "Modified well.")
                return redirect('/ppr/people')
    else:
        people_first = People.objects.get(id=1)
        if request.user.level == '0':
            form = PeopleForm(instance=people_first)
            # 같은 notice_write 페이지를 쓰되, 버튼 변경을 위해 아래를 구현
            context = {
                'form': form,
                'edit': 'Save',  # 버튼의 텍스트 값
            }
            return render(request, "ppr/modifyContent.html", context)
        else:
            messages.error(request, "You have no access.")
            return redirect('/ppr/people')

    return render(request, 'ppr/modifyContent.html')