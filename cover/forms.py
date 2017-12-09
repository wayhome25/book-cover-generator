from urllib.parse import urlencode

from django import forms


class CoverForm(forms.Form):
    title = forms.CharField(required=True, initial='default title')
    top_text = forms.CharField(required=True)
    author = forms.CharField(required=True)

    @property
    def get_params(self):
        if hasattr(self, 'cleaned_data'):
            return urlencode(self.cleaned_data)
        return None
