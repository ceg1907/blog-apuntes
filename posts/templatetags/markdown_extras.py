import markdown as md
import nh3
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def markdown(texto):
    html = md.markdown(texto, extensions=['fenced_code', 'nl2br'])
    return mark_safe(nh3.clean(html))
