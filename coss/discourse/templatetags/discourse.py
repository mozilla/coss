from datetime import timedelta
from dateutil.parser import parse

from django import template
from django.utils.timezone import now

register = template.Library()


@register.filter
def activity(date_str):
    if date_str is None:
        return ''
    d = parse(date_str)
    return date_to_activity_str(d)


def date_to_activity_str(d):
    n = now()
    delta = n - d
    if delta < timedelta(seconds=3600):
        activity_str = f'{delta.seconds//60}m'
    elif delta < timedelta(days=1):
        activity_str = f'{delta.seconds//3600}h'
    elif delta < timedelta(days=10):
        activity_str = f'{delta.days}d'
    elif d.year != n.year:
        activity_str = d.strftime('%b ’%y')
    else:
        activity_str = d.strftime('%b %d')
    return activity_str


@register.inclusion_tag('discourse/tags/discourse_latest.html')
def discourse_latest(category):
    return {'topics': category.latest_topics}
