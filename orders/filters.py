import django_filters
from .models import Objects, Requests, Brigadir
from django import forms

class RequestFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', widget=forms.DateInput(attrs={'class': "form-control ", 'type':"date", }), lookup_expr='gt')
    class Meta:
        model = Requests
        fields = ['date']
        widgets = {
            'date': forms.DateInput(attrs={'class': "form-control col-xs-2", 'type':"date", 'field_name': 'date',}),
            }
        