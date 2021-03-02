from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(error_messages={'required': 'This field is required.'}, required=True)
    released_on = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        fields = "__all__"
        model = Movie
