# apps/your_app/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def thousand_separator(value):
    try:
        return f"{value:,.2f}"
    except (ValueError, TypeError):
        return value
