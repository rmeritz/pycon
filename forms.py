- Django Forms:
  + Validation defaults all match the DB validations automatically
  + Can override the default validations that are just on the model
  ... ? I don't really understand how/where validations work in rails

  Django Forms:
  1) preparing and restructuring data ready for rendering
  2) creating HTML forms for the data
  3) receiving and processing submitted forms and data from the client

>>> f = ContactForm()
>>> f.as_ul()
u'<li><label for="id_subject">Subject:</label> <input id="id_subject" type="text" name="subject" maxlength="100" /></li>\n<li><label for="id_message">Message:</label> <input type="text" name="message" id="id_message" /></li>\n<li><label for="id_sender">Sender:</label> <input type="email" name="sender" id="id_sender" /></li>\n<li><label for="id_cc_myself">Cc myself:</label> <input type="checkbox" name="cc_myself" id="id_cc_myself" /></li>'

  {{ form.as_p }}

  {{ form.as_ul }}

Rails Forms:
  - http://guides.rubyonrails.org/form_helpers.html
  - https://github.com/plataformatec/simple_form
  - Simple Form


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
