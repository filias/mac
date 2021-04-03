# -*- coding: utf-8 -*-
import re
import datetime
from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return "active"
    return ""


@register.simple_tag
def display_none(request, pattern):
    if re.search(pattern, request.path):
        return "display:block"
    return "display:none"
