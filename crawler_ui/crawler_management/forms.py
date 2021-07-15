from django import forms
from crawler_management.models import *
from upload_validator import FileTypeValidator
from django.core.validators import FileExtensionValidator
import os
from django.core.exceptions import ValidationError

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings

        fields = ['ip', 'port', 'location']
        widgets = {
            'ip': forms.TextInput(attrs={'class':'form-control'}),
            'port': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
        }
        # this function will be used for the validation
    # def clean(self):

    #     # data from the form is fetched using super function
    #     super(SettingsForm, self).clean()

    #     # extract the username and text field from the data
    #     ip = self.cleaned_data.get('ip')
    #     port = self.cleaned_data.get('port')
    #     location = self.cleaned_data.get('location')

    #     # conditions to be met for the username length
    #     # if len(ip) > 2:
    #     #     self.add_error('ip','Maksimum 15 characters required')
    #     # if len(port) != 2:
    #     #     self.add_error('port','Equal to 2 characters required')
    #     # if len(location) > 2:
    #     #     self.add_error('location','Maksimum 25 characters required')

    #     # return any errors if found
    #     return self.cleaned_data
class CrawlerLinksForm(forms.ModelForm):
    choices = [(0,"Pasif"),(1,"Aktif")]
    status = forms.ChoiceField(choices = choices, required = True, widget = forms.Select(attrs = {'class':'form-control'}))
    class Meta:
        model = CrawlerLinks

        fields = ['start_url','status']

        widgets = {
            'start_url': forms.TextInput(attrs={'class':'form-control'}),
        }

    # def clean(self):
    #     super(CrawlerLinksForm, self).clean()

    #     start_url = self.cleaned_data.get('start_url')

    #     if len(start_url) > 2:
    #         raise forms.ValidationError({"start_url": "raise an error"})

        # return self.cleaned_data

class AssignLinkToCrawlerForm(forms.Form):
        crgs = CompanyReportGroups.objects.using('bzsaas').values_list('id','name')
        crawlers = Crawlers.objects.using('bzsaas').order_by('id').values_list('id', 'spider_name')

        crawler_ids = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices = [(x[0],x[0]) for x in crawlers]
        )

        fields = ['crawler_ids']

        crgs = forms.ChoiceField(choices = crgs, required = True, label = 'Company Report Groups', widget = forms.Select(attrs = {'class':'form-control'}))
        link_excel = forms.FileField(required = True, label='Select a excel file', validators=[FileExtensionValidator( ['xlsx','xls'] ) ])
