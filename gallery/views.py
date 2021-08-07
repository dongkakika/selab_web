from django.shortcuts import render
from .forms import GalleryForm
from .models import Gallery
from main.decorators import login_message_required
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def gallery(request):

    gallery_all = Gallery.objects.all()

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
