# app/views/jobs/_form.html.erb

<%= form_for(@job) do |f| %>
  <%= f.error_notification %>

  <div class="form-inputs">
    <%= f.input :name, as: :string  %>
    <%= f.input :description %>
    <%= f.input :company_name, as: :string %>
    <%= f.input :url, as: :url %>
    <%= f.input :start_date, as: :date %>
  </div>

  <div class="form-actions">
    <%= f.button :submit %>
  </div>
<% end %>


### Notes:
# * There is no form class
# * fields are explicately called by name in the view
# * Validation spread in the schema/model and controller??
# * All the information a designer would want is closer at hand
# * http://guides.rubyonrails.org/form_helpers.html
# * https://github.com/plataformatec/simple_form
# * Laison, draper, effigy - Presenter/Form Objects
# * http://api.rubyonrails.org/classes/ActionView/Helpers/FormBuilder.html
