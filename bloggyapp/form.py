from django import forms

class SubscriberForm(forms.Form):
    email = forms.EmailField(required=True,
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))





class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
