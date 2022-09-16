# from django import forms
# from .models import Requests

# class RequestsModelForm(forms.ModelForm):
#     class Meta:
#         model = Requests

#     def __init__(self, *args, **kwargs):
#         forms.ModelForm.__init__(self, *args, **kwargs)
#         self.fields['date'].queryset = Requests.avail.all()