from django import forms

class EnquiryForm(forms.Form):
    name = forms.CharField(label="Name:")
    email = forms.EmailField()
    subject = forms.CharField(label="Subject:")
    message = forms.CharField(max_length=10000)