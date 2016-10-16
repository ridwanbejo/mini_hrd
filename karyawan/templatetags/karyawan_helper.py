from django import template
import os

register = template.Library()

@register.filter
def get_filename(value):
    return os.path.basename(value.path)