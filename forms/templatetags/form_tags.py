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