from django.shortcuts import render
import wtforms

from .models import APIPage

def add_application(request):

    class APISubscriptionForm(wtforms.Form):
        api = wtforms.SelectField("Subscribe to an API", default=0,
            choices=[(0, '---')], coerce=int)

    class ApplicationForm(wtforms.Form):
        name = wtforms.StringField('name', [wtforms.validators.Length(min=5, max=300),
                                            wtforms.validators.InputRequired()])
        description = wtforms.TextAreaField('description', [wtforms.validators.optional()])
        location = wtforms.StringField('homepage location', [wtforms.validators.URL(),
                                                    wtforms.validators.optional()])

        subscribe = wtforms.FieldList(wtforms.FormField(APISubscriptionForm), min_entries=1)

    if request.POST:
        form = ApplicationForm(request.POST)
        add_extra(form)
    else:
        form = ApplicationForm()

    # All entries fields share their choices apparently
    form.subscribe.entries[0].api.choices.extend([(api.pk, api.name) for api in APIPage.objects.all()])
    subs = ((1, 'Vanha respa'), (2, 'Toinen API'))


    return render(request, 'apimanager/api_formi.html', {'form': form, 'subscriptions' : subs})

def add_extra(form):
    if form.subscribe.entries[-1].api.data:
        form.subscribe.append_entry()
