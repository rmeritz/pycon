# templates/base/form.html
<form action="{% url create_job %}" method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}

    <div class="form-inputs">
        {{ form.as_p }}
    </div>

    <div class="form-actions">
        <input type="submit" value="Submit"/>
    </div>
</form>


# jobs/forms.py

from django import forms

from crazy_widgets import CrazyTextInput

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["name", "description", "start_date"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self._is_name_obscence(name):
            raise forms.ValidationError('You may not choose an obscene name')
        return email

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget = CrazyTextInput()


### Notes:
# * Django Forms handle many aspects of handling data in one place
# 1) preparing and restructuring data ready for rendering
# 2) creating HTML forms for the data
# 3) receiving and processing submitted forms and data from the client

### Notes:
# Django Widgets:
# * reusable and can be packaged easilly in a third party library
# * hard to see from the html what the form is actually doing
# * can be hard for a non-programming designer to get there hands around things
