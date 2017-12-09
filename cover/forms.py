from django import forms


class CoverForm(forms.Form):
    title = forms.CharField(required=True, initial='default title')
    top_text = forms.CharField(required=True)
    author = forms.CharField(required=True)
