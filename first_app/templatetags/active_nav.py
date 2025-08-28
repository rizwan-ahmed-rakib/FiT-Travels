# from django import template
#
# register = template.Library()
#
#
# @register.simple_tag
# def active(request, url_name):
#     if request.path == url_name:
#         return "bg-[#A80001]"  # Return the class to highlight the nav item
#     return ""


# first_app/templatetags/active_nav.py
from django import template
import re

register = template.Library()

@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return "bg-[#A80001]"  # Return the class to highlight the nav item
    return ""
