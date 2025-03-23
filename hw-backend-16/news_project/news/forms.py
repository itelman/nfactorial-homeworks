from django import forms

from .models import Comment
from .models import News
from django import forms
from django.contrib.auth.models import User,Group


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            user.groups.add(Group.objects.get(name="default"))  # Assign default group
        return user
