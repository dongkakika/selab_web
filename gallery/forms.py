from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({
            'placeholder': 'Please upload an image',
            'class': 'form-control',
            'type': 'file',
            'autofocus': True,
        })
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Please make the content',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Gallery
        fields = ['title', 'img', 'content',]