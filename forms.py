# jobs/forms.py
from datetime import timedelta

from django import forms
from obscene import is_obscene

from .models import Job


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["name", "description", "start_date"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if is_obscene(name):
            raise forms.ValidationError('You may not choose an obscene name')
        return name

    def save(self, *args, **kwargs):
        kwargs.update({'commit': False})
        job = super(JobCreateForm, self).save(*args, **kwargs)
        job.end_date = job.start_date + timedelta(days=30)
        job.save
        return job


### Notes:
# * Django Forms handle many aspects of handling data in one place
# 1) preparing and restructuring data ready for rendering
# 2) creating HTML forms for the data
# 3) receiving and processing submitted forms and data from the client
# * Self is
