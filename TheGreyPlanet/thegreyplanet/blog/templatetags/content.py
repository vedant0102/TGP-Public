from django import template

register = template.Library()

from ..models import Content


@register.simple_tag
def content(content_for) :
    return Content.objects.get(content_for=content_for).content