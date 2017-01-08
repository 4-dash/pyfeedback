# coding=utf-8

from django.conf import settings
from django.views.decorators.http import require_safe
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView

from feedback.models import Veranstaltung
from feedback.forms import VeranstaltungEvaluationForm  # , VeranstaltungBasisdatenForm


# TODO: Ist diese Funktion noch noetig ??
@require_safe
def login(request):
    if 'vid' in request.GET and 'token' in request.GET:
        vid = int(request.GET['vid'])
        token = unicode(request.GET['token'])

        user = auth.authenticate(vid=vid, token=token)
        if user:
            auth.login(request, user)
            v = Veranstaltung.objects.get(id=vid)
            request.session['vid'] = v.id
            request.session['veranstaltung'] = unicode(v)

            if v.status is Veranstaltung.STATUS_BESTELLUNG_LIEGT_VOR or Veranstaltung.STATUS_BESTELLUNG_GEOEFFNET:
                return HttpResponseRedirect(reverse('veranstalter-index'))

    return render(request, 'veranstalter/login_failed.html')


VERANSTALTER_VIEW_TEMPLATES = {
    "evaluation": "formtools/wizard/evaluation.html",
    # "basisdaten": "formtools/wizard/basisdaten.html",
}


def process_vollerhebung(context, data):
    if context['veranstaltung'].semester.vollerhebung:
        data._mutable = True
        data['evaluation-evaluieren'] = True
        data._mutable = False


def show_summary_form_condition(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('evaluation') or {}
    return cleaned_data.get('evaluieren', True)


class VeranstalterWizard(SessionWizardView):
    # TODO: Login und bestellung_erlaubt beachten

    form_list = [
        ('evaluation', VeranstaltungEvaluationForm),
        # ('basisdaten', VeranstaltungBasisdatenForm),
    ]

    def get_context_data(self, form, **kwargs):
        if self.request.user.username != settings.USERNAME_VERANSTALTER:
            return render(self.request, 'veranstalter/not_authenticated.html')

        context = super(VeranstalterWizard, self).get_context_data(form=form, **kwargs)
        context.update({'veranstaltung': Veranstaltung.objects.get(id=self.request.session['vid'])})
        return context

    def get_form(self, step=None, data=None, files=None):
        form = super(VeranstalterWizard, self).get_form(step, data, files)
        if step is None:
            step = self.steps.current

        if step == 'evaluation':
            if data is not None:
                process_vollerhebung(self.get_context_data(form), data)

        return form

    def get_template_names(self):
        return [VERANSTALTER_VIEW_TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        instance = Veranstaltung.objects.get(id=self.request.session['vid'])
        save_to_db(instance, form_list)
        return render_to_response('formtools/wizard/zusammenfassung.html', {'form_data': form_data,
                                                                            'form_list': form_list})


def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    return form_data


def save_to_db(instance, form_list):
    for form in form_list:
        for key, val in form.cleaned_data.iteritems():
            setattr(instance, key, val)
    instance.save()
    set_veranstaltung_status(instance)


def set_veranstaltung_status(instance):
    instance.set_next_state()
    instance.save()



