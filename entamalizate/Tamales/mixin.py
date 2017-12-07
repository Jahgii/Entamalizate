from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):

    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Se debe iniciar sesion para hacer esta accion"] )
            return self.form_invalid(form)