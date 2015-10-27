from django.shortcuts import render
import django.forms as forms

from .models import APIPage

def add_application(request):

    class ApplicationForm(forms.Form):
        name = forms.CharField(label='name')
        description = forms.CharField(label='description', widget=forms.Textarea)
        location = forms.URLField(label='homepage location')

        subscribe = forms.MultipleChoiceField(label="Subscribe to an API", choices=get_api_choices,
                                              widget=forms.CheckboxSelectMultiple)

    if request.POST:
        form = ApplicationForm(request.POST)
    else:
        form = ApplicationForm()

    # All entries fields share their choices apparently

    subs = ((1, 'Vanha respa'), (2, 'Toinen API'))

    return render(request, 'apimanager/api_formi.html', {'form': form, 'subscriptions' : subs})

def get_api_choices():
    return [(api.pk, api.name) for api in APIPage.objects.all()]