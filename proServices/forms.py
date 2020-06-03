from django import forms

PHOTOS_SERVICES = [
    ("Simple photo editing", "Simple photo editing"),
    ("Photo Restoration", "Photo Restoration"),
    ("Weeding Photo Editing", "Weeding Photo Editing"),
    ("Background Removal", "Background Removal"),
    ("Drop Shadow", "Drop Shadow"),
    ("Other", "Other"),
]


class PhotoQuoteForm(forms.Form):
    name = forms.CharField(required=True, max_length=90)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=40)
    photoService = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=PHOTOS_SERVICES,
        label="Service Selection",
    )
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows": 4}))
