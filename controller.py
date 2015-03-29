#job/views.py
from django.views.generic import CreateView

from .models import Job
from .forms import CreateJobForm


class JobCreateView(CreateView):
    model = Job
    form_class = CreateJobForm


# django/django/blob/1.7/django/views/generic/edit.py
class CreateView
    ...

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


### Notes:
# * Class Based Views are awesome
# * Can easily package views for third-party apps
# * Easy for someone to modify any small part of their behavoir
# * Instead of creating a Rails Engine
