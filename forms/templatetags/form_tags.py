from django import template

register = template.Library()

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        else:
            css_class = 'is-valid'
        
    return 'form-control form-control-sm {0}'.format(css_class)

@register.simple_tag
def password_error(error, field):
    base_str = "The {0} field is required"
    if error == "This field is required.":
        field_name = "password" if field.name == "password1" else "password confirmation" if field.name == "password2" else field.name
        return base_str.format(field_name)