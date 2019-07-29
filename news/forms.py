# from django import forms
# from .models import  Category,Comment,News
# class NewsAddForm(forms.ModelForm):
#     class Meta:
#         model=News
#         fields='__all__'
# class NewsUpdateForm(forms.ModelForm):
#     class Meta:
#         model=News
#         fields=('location','description','author','categories')
from django import forms
from .models import Comment,News
class inputForm(forms.Form):
     forms1=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'id':'search','placeholder':'search here'}))

class CommentForm(forms.ModelForm):
     class Meta:
          model=Comment
          fields=('title',)
     title=forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class':'f','placeholder':'Add Comments'}))
class newsform(forms.ModelForm):
     class Meta:
          model=News
          fields=('headline','description','author','url','picture')
     headline=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'f'}))
     description=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class':'n'}))
     author=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'f'}))
     url=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'f'}))
     picture=forms.ImageField(max_length=200,widget=forms.FileInput(attrs={'class':'m'}))