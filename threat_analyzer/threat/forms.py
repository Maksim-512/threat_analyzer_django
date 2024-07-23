from django import forms


class TextInputForm(forms.Form):
    input_str = forms.CharField(widget=forms.Textarea)
