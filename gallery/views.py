from django.shortcuts import render
from .forms import GalleryForm
from .models import Gallery
from main.decorators import login_message_required
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def temp(request):
    gallery_all = Gallery.objects.all().order_by('-id')
    context = {
        'gallery_all': gallery_all,
    }
    return render(request, "gallery/temp.html", context)


def gallery(request):
    gallery_all = Gallery.objects.all().order_by('-id')
    context = {
        'gallery_all': gallery_all,
    }
    return render(request, 'gallery/gallery.html', context)

@login_message_required
def gallery_add(request):
    if request.method == "POST":
        form = GalleryForm(request.POST)
        if form.is_valid():
            # commit = False는 바로 저장하는 것을 방지
            research = form.save(commit=False)
            if request.POST.get('img', True):
                research.img = request.FILES['img']
            messages.success(request, "Uploaded successfully")
            research.save()
            return redirect('gallery:gallery')
        else:
            messages.success(request, "error")
            return redirect('gallery:gallery')

    else:
        form = GalleryForm()
        return render(request, 'gallery/gallery_add.html', {'form': form})

@login_message_required
def gallery_delete(request, pk):
    gallery = Gallery.objects.get(id=pk)
    if request.user.level == '0' or request.user.level == '1':
        gallery.delete()
        return redirect('gallery:gallery')
    else:
        messages.error(request, 'You have no access.')
        return redirect('gallery:gallery')


@login_message_required
def gallery_modify(request, pk):
    gallery_current = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        if request.user.level == '0' or request.user.level == '1':
            form = GalleryForm(request.POST, instance=gallery_current)
            if form.is_valid():
                gallery = form.save(commit=False)
                # ** 수정할 때도 사진은 따로 변경해줘야 함
                if request.POST.get('img', True):
                    gallery.img = request.FILES['img']
                    # People.objects.get(id=pk).img_upload.delete() # 이전 사진 삭제
                messages.success(request, "Modified well")
                gallery.save()
                return redirect('gallery:gallery')

    else:
        gallery = Gallery.objects.get(id=pk)
        if request.user.level == '0' or request.user.level == '1':
            form = GalleryForm(instance=gallery)
            context = {
                'form': form,
                'gallery': gallery,
                'edit': 'Modify',  # 버튼의 텍스트 값
            }
            return render(request, 'gallery/gallery_add.html', context)
        else:
            messages.error(request, "You do not have access")
            return redirect('gallery:gallery')