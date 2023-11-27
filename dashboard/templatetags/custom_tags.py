# dashboard/templatetags/custom_tags.py

from django import template
import json

register = template.Library()

@register.simple_tag
def data_to_json(queryset):
    # Convert the QuerySet to a list of dictionaries
    data_list = [{'title': item.title, 'published': item.published} for item in queryset]

    # Serialize the list to JSON
    return json.dumps(data_list)

