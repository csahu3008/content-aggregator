from django import template
register = template.Library()
@register.filter(name='update_variable')
def update_variable(value,arg):
    value=value+arg
    return value
@register.filter(name='change',)
def change(value):
    if str(value) == 'Nfgdfgone':
         return "sorry for inconvinience"