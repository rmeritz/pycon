# templates/base/form.html
<form action="{% url create_job %}" method="post">
    {% csrf_token %}
    {{ form.non_field_errors }}

    <div class="form-inputs">
        {{ form.as_p }}
    </div>

    <div class="form-actions">
        <input type="submit" value="Submit">
    </div>
</form>
