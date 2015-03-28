# jobs/forms.py

from django import forms
from ..craz


class JobForm(forms.ModelForm):
    class Meta:
        model = EquityCampaign
        fields = ["name", "description", "start_date"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self._is_name_obscence(name):
            raise forms.ValidationError('You may not choose an obscene name')
        return email

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget = MyCrazyTextInput()


### Notes:
# * Django Forms handle many aspects of handling data in one place
# 1) preparing and restructuring data ready for rendering
# 2) creating HTML forms for the data
# 3) receiving and processing submitted forms and data from the client

>>> f = ContactForm()
>>> f.as_ul()
u'<li><label for="id_subject">Subject:</label> <input id="id_subject" type="text" name="subject" maxlength="100" /></li>\n<li><label for="id_message">Message:</label> <input type="text" name="message" id="id_message" /></li>\n<li><label for="id_sender">Sender:</label> <input type="email" name="sender" id="id_sender" /></li>\n<li><label for="id_cc_myself">Cc myself:</label> <input type="checkbox" name="cc_myself" id="id_cc_myself" /></li>'

  {{ form.as_p }}

  {{ form.as_ul }}

<form enctype="{% block form-page-enctype %}{% endblock %}" action="{% block form-page-action %}{% endblock %}" method="post" data-selenium="page-form">
    {% csrf_token %}
    {{ form.non_field_errors }}

    {% for hidden in form.hidden_fields %}
        {{ hidden }}
    {% endfor %}

    {% for field in form.visible_fields %}
        <div class="form-field">
            {{ field.errors }}
            {{ field.label_tag }}
            {{ field }}
        </div>
    {% endfor %}
    <div class="l-submit">
      <input type="submit" value="{% block form-page-submit %}Submit{% endblock %}" class="btn btn-strong btn-direction" />
  </div>
{% endblock form-page-button %}
</form>


- Django Widgets:
 + reusable and can be packaged easilly in a third party library
 - hard to see from the html what the form is actually doing
 - can be hard for a non-programming designer to get there hands around things
