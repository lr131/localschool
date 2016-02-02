from django import forms

from .models import Post, Rasp, UploadFile

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control' 
            
    class Meta:
        model = Post
        fields = ('text',)
        
        
#widget=forms.TextInput
class RaspForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RaspForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control' 
            
    class Meta:
        model = Rasp
        fields = ('class_name','weekday', 'lesson', 'org_day', )
        

class UploadFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control' 
    class Meta:
        model = UploadFile
        fields = ('name','fileplan', )