from django.shortcuts import render
import django.forms as forms

from .models import APIPage

def get_api_choices():
    return [(api.pk, api.name) for api in APIPage.objects.all()]

class ApplicationForm(forms.Form):
    name = forms.CharField(label='name')
    description = forms.CharField(label='description', widget=forms.Textarea)
    location = forms.URLField(label='homepage location', required=False)

    subscribe = forms.MultipleChoiceField(label="Subscribe to an API", choices=get_api_choices,
                                          widget=forms.CheckboxSelectMultiple, required=False)

def add_application(request):

    ask_save = False
    if request.POST:
        app_form = ApplicationForm(request.POST)
        if request.POST.get('save_ok') and app_form.is_valid():
            register(app_form.cleaned_data)
        elif request.POST.get('save') and app_form.is_valid():
            ask_save = True
    else:
        app_form = ApplicationForm()

    # All entries fields share their choices apparently

    subs = ((1, 'Vanha respa'), (2, 'Toinen API'))

    return render(request,
                  'apimanager/api_formi.html',
                  {'form': app_form, 'subscriptions' : subs, 'ask_save': ask_save})

def register(data):
    print('registering')
