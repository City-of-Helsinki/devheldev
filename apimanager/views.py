from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import django.forms as forms

from .models import APIPage, Application, APISubscription


def get_api_choices(user):
    all_apis = set([(api.pk, api.name) for api in APIPage.objects.all()])
    subs = set([(api.pk, api.name) for api in APISubscription.objects.filter(user=user)])


class ApplicationForm(forms.Form):

    def __init__(self, user, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['subscribe'] = forms.ModelMultipleChoiceField(
            APIPage.objects.exclude(kongapiconfiguration__apisubscription__application__user=user),
            label="Subscribe to an API",
            widget=forms.CheckboxSelectMultiple,
            required=False)

    name = forms.CharField(label='name', required=True)
    description = forms.CharField(label='description', widget=forms.Textarea,
                                  required=True)
    location = forms.URLField(label='homepage location', required=False)


def register(data, user, app=False):
    """
    Register application or update it

    :param data: Form data
    :type data: dict
    :param user: Django user model
    :type user: User
    :param app: existing Application instance
    :type app: Application
    :return: None
    :rtype: None
    """

    if not app:
        app = Application.objects.create(
            user=user,
            name=data['name'],
            description=data['description'],
            location=data['location']
        )
    else:
        app.name = data.get('name')
        app.description = data['description']
        app.location = data['location']
        app.save()

    for sub in data['subscribe']:
        api = APIPage.objects.get(pk=sub)
        apisub = APISubscription(
            api=api.kongapiconfiguration,
            application=app
        )
        apisub.save()


def unsubscribe(data, user):
    sub_id = data.get('unsubscribe')
    sub = APISubscription.objects.get(pk=sub_id, api__apisubscription__application__user=user)
    sub.delete()
    return sub


@login_required
def add_application(request):

    ask_save = False
    msg = None
    if request.POST:
        if request.POST.get('unsubscribe'):
            sub = unsubscribe(request.POST, request.user)
            return HttpResponseRedirect(reverse('apimanager:view_applications'))
        else:
            app_form = ApplicationForm(request.user, request.POST)
            if request.POST.get('save_ok') and app_form.is_valid():
                register(app_form.cleaned_data, request.user)
                return HttpResponseRedirect(reverse('apimanager:view_applications'))
            elif request.POST.get('save') and app_form.is_valid():
                ask_save = True
    else:
        app_form = ApplicationForm(request.user)

    return render(request,
                  'apimanager/api_formi.html',
                  {'form': app_form, 'ask_save': ask_save})


@login_required
def view_applications(request):

    apps = Application.objects.all()

    return render(request,
                  'apimanager/api_app_list.html',
                  {'apps': apps})


@login_required
def update_application(request, app_id):
    ask_save = False
    app = Application.objects.get(pk=app_id, user=request.user)

    if request.POST:
        if request.POST.get('unsubscribe'):
            sub = unsubscribe(request.POST, request.user)
            return HttpResponseRedirect(reverse('apimanager:view_applications'))
        else:
            app_form = ApplicationForm(request.user, request.POST)
            if request.POST.get('save_ok') and app_form.is_valid():
                register(app_form.cleaned_data, request.user, app)
                return HttpResponseRedirect(reverse('apimanager:view_applications'))
            elif request.POST.get('save') and app_form.is_valid():
                ask_save = True
    else:
        app_form = ApplicationForm(request.user, {
            "name": app.name,
            "description": app.description,
            "location": app.location})

    subs = APISubscription.objects.filter(api__apisubscription__application__user=request.user)

    return render(request,
                  'apimanager/api_formi.html',
                  {'form': app_form, 'subscriptions': subs, "app": app, 'ask_save': ask_save})
