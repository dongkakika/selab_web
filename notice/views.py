from django.shortcuts import render

# 공지사항 게시판의 전체 게시글을 표시하기 위해,
# Django에서 제공하는 Generic display views 중 ListView를 사용한다.
# notice앱 내 views.py에 ListView를 import하고 아래의 소스를 입력한다.
from django.views.generic import ListView
from .models import Notice

from django.contrib import messages # get_queryset 하단부에서 에러 처리를 위해 사용
from django.db.models import Q # 제목 + 내용 타입과 같이 두 가지 이상의 필터 조건을 적용하기 위해 Q를 import

from main.decorators import login_message_required
from django.shortcuts import get_object_or_404

from main.models import User
from django.shortcuts import redirect
from.forms import NoticeWriteForm
from main.decorators import admin_required

# -------------------- ip 주소 얻기 --------------------
from ipware.ip import get_client_ip

# get_client_ip 함수는 아래와 같은 로직으로 되어 있다.
#def get_client_ip(request):
#    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#    if x_forwarded_for:
#        ip = x_forwarded_for.split(',')[0]
#    else:
#        ip = request.META.get('REMOTE_ADDR')
#    return ip

# -------------------- 게시판 글 변경, 삭제 --------------------
# 글 변경
@login_message_required # 로그인한 사용자만
def notice_edit_view(request, pk):
    notice = Notice.objects.get(id=pk)

    if request.method == "POST":
        # 작성자 검사, 관리자 검사 --> 둘만 수정 가능
        if (notice.writer == request.user or request.user.level == '0'):
            # 기존의 제목과 내용 등 값들을 그대로 넘겨주기 위해 instance=notice(객체)로 넘김
            form = NoticeWriteForm(request.POST, instance=notice)
            if form.is_valid():
                notice = form.save(commit=False)
                notice.save()
                messages.success(request, "Modified well.")
                return redirect('/notice/' + str(pk))
    else:
        notice = Notice.objects.get(id=pk)
        if notice.writer == request.user or request.user.level == '0':
            form = NoticeWriteForm(instance=notice)
            # 같은 notice_write 페이지를 쓰되, 버튼 변경을 위해 아래를 구현
            context = {
                'form': form,
                'edit': 'Save', # 버튼의 텍스트 값
            }
            return render(request, "notice/notice_write.html", context)
        else:
            messages.error(request, "This post does not belong to you.")
            return redirect('/notice/' + str(pk))

# 글 삭제
@login_message_required
def notice_delete_view(request, pk):
    notice = Notice.objects.get(id=pk)
    if notice.writer == request.user or request.user.level == '0':
        notice.delete()
        messages.success(request, "Deleted successfully.")
        return redirect('/notice/')
    else:
        messages.error(request, "This post does not belong to you.")
        return redirect('/notice/'+str(pk))


# -------------------- 게시판 글 쓰기 --------------------
# 관리자인 사용자만 글 작성 가능
# 로그인해야 글 작성 가능
# 앞에서 생성한 forms.py의 NoticeWriteForm을 GET으로 뿌려주고,
# 입력된 폼 값들이 POST로 요청되면,
# user 변수에 접속 사용자의 세션 아이디를 담아
# 모델의 작성자 필드에 삽입

@login_message_required
def notice_write_view(request):
    if request.method == "POST":
        form = NoticeWriteForm(request.POST)
        user = request.session['userid']
        userid = User.objects.get(userid=user)

        if form.is_valid():
            notice = form.save(commit = False) # 커밋 --> False
            notice.writer = userid # 작성자
            notice.save() # 내용 저장
            return redirect('notice:notice_list')
    else:
        form = NoticeWriteForm()

    return render(request, "notice/notice_write.html", {'form': form})

# -------------------- 게시글 좋아요 --------------------
from django.http import HttpResponse # import
def like_notice(request, pk):
    #messages.success(request, "호출")
    notice = get_object_or_404(Notice, pk=pk)
    notice.like_count += 1
    notice.save()
    return HttpResponse('Like')

def cancel_like_notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.like_count -= 1
    notice.save()
    return HttpResponse('Cancel')


# -------------------- 게시판 글 읽기 --------------------
# 1번
def notice_detail_view(request, pk):
    notice = get_object_or_404(Notice, pk=pk)

    # 추가: 작성자 본인이 아니면 수정과 삭제 버튼을 보이지 않게
    if request.user == notice.writer:
        notice_auth = True
    else:
        notice_auth = False

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # messages.success(request, ip) # 확인

    context = {
        'notice': notice,
        'notice_auth': notice_auth,
        'looog': ip,
    }
    # 조회수 증가
    notice.hits += 1
    notice.save()

    # 좋아요 증가
    if(request.GET.get('like_notice')):
        notice.like_count += 1
        notice.save()

    return render(request, 'notice/notice_detail.html', context)


# -------------------- 이하 게시판 뷰, 검색 기능 --------------------

# Create your views here.
class NoticeListView(ListView):
    model = Notice
    paginate_by = 9
    template_name = 'notice/notice_list.html'   #DEFAULT : <app_label>/<model_name>_list.html
    context_object_name = 'notice_list'         #DEFAULT : <model_name>_list

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '') # 2. +검색 기능, search_keyword에 파라미터1 저장
        search_type = self.request.GET.get('type', '') # 2. +검색 기능, search_type   에 파라미터2 저장
        notice_list = Notice.objects.order_by('-id') # 1. 게시글 --> 게시글 등록 순서대로 나열 (id사용)

        # 2. +검색 기능,
        # Django의 query filter 기능을 사용, 템플릿(이하의 html)에서 select 태그로 종류별 검색어를 받아 from GET 메소드로 요청 사용
        # view에서 form의 값들이 GET으로 넘어와,
        # url 뒤에 /?type=’검색타입’&q=’검색어’&page=’페이지’와 같은 형식으로 파라미터들을 받게 되면,
        # request 객체에 있는 get은 딕셔너리 형으로 변환하여 저장하게 된다.
        # 따라서 request.GET.get(‘파라미터값’, ‘ ‘)와 같은 형식으로 파라미터를 전달받고
        # 쿼리 필터를 적용하여 반환하는 소스를 이전 포스팅에서 구현한 NoticeListView의 get_queryset에 아래와 같이 추가
        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_notice_list = notice_list.filter(
                        # 전체 쿼리셋에서 search_keyword가 포함되어있는 쿼리셋만 가져오기 위해
                        # ‘필드명’__icontains = ‘조건값’ 형식으로 필터를 적용합니다.
                        # __icontains는 대소문자를 구분하지 않고 조건값이 포함되어 있는 데이터를 가져온다.
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__userid__icontains=search_keyword)) # 실제 db에 있는 user의 userid이다. *주의: 잘못 입력하면 error
                elif search_type == 'title_content':
                    search_notice_list = notice_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_notice_list = notice_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_notice_list = notice_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_notice_list = notice_list.filter(writer__userid__icontains=search_keyword) # 실제 db에 있는 user의 userid이다.

                return search_notice_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return notice_list
    # 게시글의 리스트를 '최근 작성순'으로 표시하기 위해 get_queryset 메소드를 '오버라이딩'하여 order_by로 정렬을 한 후 쿼리셋을 반환.
    # Django의 ListView를 사용하면 따로 Paginator를 import할 필요없이,
    # paginate_by로 한 페이지에 표시할 게시글의 개수를 정할 수 있다.
    # 또한 DEFAULT로 template_name과 context_object_name이 정해져 있기에,
    # 템플릿에서 < model_name >_list로 쿼리셋을 사용할 수 있다.

    # 페이지 숫자 버튼을 커스텀하기 위해 get_context_data 메소드로 페이지 숫자 범위 context를 생성해 템플릿에 전달
    # 따로 view를 생성 않고, NoticeView내에 아래와 같이 get_context_data 메소드를 추가
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        # 2. +검색 기능
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        # 3. + 상단 고정 --> 필터를 걸어서 top_fixed가 True인 게시글 쿼리셋을 가져와서 아~래의 context에 추가
        notice_fixed = Notice.objects.filter(top_fixed=True).order_by('-registered_date')

        # 2. + 검색 기능 (검색 타입을 유지하기 위해 context를 이용해 'q', 'type', 'notice_fixed' 태그(?)에 순서대로 저장!)
        # 참고로 context는 dictionary 타입이다!
        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type
        # 3. + 상단 고정
        context['notice_fixed'] = notice_fixed

        return context