from django import forms


class PhotoQuoteForm(forms.Form):
    name = forms.CharField(required=True, max_length=90)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=40)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows": 4}))