from django import forms
from django.core.mail import send_mail
from .models import Post, Comment


class PostShareForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    post = forms.ModelChoiceField(
        queryset=Post.published.all(), widget=forms.HiddenInput
    )

    def send_email(self):
        cd = self.cleaned_data
        post = cd["post"]

        send_mail(post.title, post.body, cd["email"], [cd["to"]])

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
