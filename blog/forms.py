from django import forms
from .models import Blogs

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'description']
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full max-w-xs',
            'placeholder': 'Type here'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'textarea textarea-bordered w-full',
            'rows': 4,
            'placeholder': 'Write your blog description here...'
        })
    )
