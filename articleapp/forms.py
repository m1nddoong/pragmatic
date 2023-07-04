from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # bootstrap 에 있는 text-left 클래스 사용, 높이 자동 조절
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto; text-align: left'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
