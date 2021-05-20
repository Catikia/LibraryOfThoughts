from django import forms
from .models import Post, Category

#select box requires double entry
#not hardcoding as it is not dynamic
#choices = [('coding'),('coding'),('art'),('art'),('music'),('music')]
#dynamic way:
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'subject', 'summary', 'thoughts')

    #adds dictionary in dictionary for form-control for formatting in bootstrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject Here'}),
            'thoughts': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter thoughts here'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter short summary of thought here'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'subject', 'summary', 'thoughts')

    #adds dictionary in dictionary for form-control for formatting in bootstrap
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of thought here'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject Here'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter short summary of thought here'}),
            'thoughts': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter thoughts here'}),
        }
