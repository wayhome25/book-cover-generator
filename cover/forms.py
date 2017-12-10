from urllib.parse import urlencode

from django import forms

from cover.utils import COLOR_CODE


class CoverForm(forms.Form):
    COLOR_CHOICES = [(i, str(COLOR_CODE[i])) for i in range(len(COLOR_CODE))]

    title = forms.CharField(required=True, initial='default title')
    top_text = forms.CharField(required=True)
    author = forms.CharField(required=True)
    animal_code = forms.ChoiceField(choices=[(i, i) for i in range(1, 41)])
    color_code = forms.ChoiceField(choices=COLOR_CHOICES)
    guide_text = forms.CharField()
    guide_text_placement = forms.ChoiceField(
            choices=[
                ('bottom_right', 'bottom_right'),
                ('bottom_left', 'bottom_left'),
                ('top_right', 'top_right'),
                ('top_left', 'top_left'),
            ])

    @property
    def get_params(self):
        if hasattr(self, 'cleaned_data'):
            return urlencode(self.cleaned_data)
        return None
