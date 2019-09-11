from django import template

register = template.Library()

@register.inclusion_tag('event_arhives.html')
def event_arhives(event):
    arhives = event
    return {'arhives': arhives}