from django.shortcuts import render
import wtforms

def add_application(request):

    class ApplicationForm(wtforms.Form):
        name = wtforms.StringField('nimi', [wtforms.validators.Length(min=5, max=300),
                                            wtforms.validators.InputRequired()])
        description = wtforms.TextAreaField('kuvaus', [wtforms.validators.optional()])

    return render(request, 'apimanager/api_formi.html', {'form':ApplicationForm()})
