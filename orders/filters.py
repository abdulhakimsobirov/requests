import django_filters
from .models import Objects, Requests, Brigadir
from django import forms

class RequestFilter(django_filters.FilterSet):
    date = django_filters.DateFilter( widget=forms.DateInput(attrs={'class': "form-control ", 'type':"date", }))
    class Meta:
        model = Requests
        fields = ['date']
        widgets = {
            'date': django_filters.DateFilter(attrs={'class': "form-control", 'type':"date", 'field_name': 'date', 'id':"accLabels"}),
            }
        