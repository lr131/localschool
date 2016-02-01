from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control' 
            
    class Meta:
        model = Post
        fields = ('text',)
        
        
#widget=forms.TextInput