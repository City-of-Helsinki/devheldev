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

        subscriptions = wtforms.FieldList(wtforms.FormField(APISubscriptionForm), min_entries=2)

    form = ApplicationForm()

    # All entries fields share their choices apparently
    form.subscriptions.entries[0].api.choices.extend([(api.pk, api.name) for api in APIPage.objects.all()])

    return render(request, 'apimanager/api_formi.html', {'form': form})
