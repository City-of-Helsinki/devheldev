from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import django.forms as forms

from .models import APIPage, Application, APISubscription


class ApplicationForm(forms.Form):

    def __init__(self, subscriptions, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        queryset = APIPage.objects.exclude(use_api_gateway=False).exclude(kongapiconfiguration=None)

        if subscriptions:
            api_pages = [sub.api.api_page.pk for sub in subscriptions]
            print(api_pages)
            queryset = queryset.exclude(pk__in=api_pages)

        self.fields['subscribe'] = forms.ModelMultipleChoiceField(
            queryset,
            label="Subscribe to an API",
            widget=forms.CheckboxSelectMultiple,
            required=False)

    name = forms.CharField(label='name', required=True)
    description = forms.CharField(label='description', widget=forms.Textarea,
                                  required=True)
    app_url = forms.URLField(label='homepage url', required=False)


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
            app_url=data['app_url']
        )
    else:
        app.name = data.get('name')
        app.description = data['description']
        app.app_url = data['app_url']
        app.save()

    for api in data['subscribe']:
        # api = APIPage.objects.get(pk=sub)
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

    msg = None
    if request.POST:
        if request.POST.get('unsubscribe'):
            sub = unsubscribe(request.POST, request.user)
            return HttpResponseRedirect(reverse('apimanager:view_applications'))
        else:
            app_form = ApplicationForm(None, request.POST)
            if app_form.is_valid():
                register(app_form.cleaned_data, request.user)
                return HttpResponseRedirect(reverse('apimanager:view_applications'))
    else:
        app_form = ApplicationForm(None)

    return render(request,
                  'apimanager/api_formi.html',
                  {'form': app_form})


@login_required
def view_applications(request):

    apps = Application.objects.filter(user=request.user)

    return render(request,
                  'apimanager/api_app_list.html',
                  {'apps': apps})


@login_required
def update_application(request, app_id):

    app = Application.objects.get(pk=app_id, user=request.user)

    if request.POST:
        if request.POST.get('unsubscribe'):
            sub = unsubscribe(request.POST, request.user)
            return HttpResponseRedirect(reverse('apimanager:view_applications'))
        else:
            app_form = ApplicationForm(app.apisubscription_set.all(), request.POST)
            if app_form.is_valid():
                register(app_form.cleaned_data, request.user, app)
                return HttpResponseRedirect(reverse('apimanager:view_applications'))
    else:
        app_form = ApplicationForm(app.apisubscription_set.all(), {
            "name": app.name,
            "description": app.description,
            "app_url": app.app_url})

    subs = APISubscription.objects.filter(application=app)

    return render(request,
                  'apimanager/api_formi.html',
                  {'form': app_form, 'subscriptions': subs, "app": app})
