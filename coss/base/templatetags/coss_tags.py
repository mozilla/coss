from django import template
from django.conf import settings
from django.utils.http import urlencode
from django.templatetags.static import static

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.active = (calling_page.path.startswith(menuitem.path)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }


@register.simple_tag(takes_context=True)
def share_page_twitter_url(context):
    base_url = 'https://www.twitter.com/intent/tweet?'
    params = {
        'text': context['page'].title,
        'url': context['page'].full_url
    }
    return base_url + urlencode(params)


@register.simple_tag(takes_context=True)
def share_page_fb_url(context):
    base_url = 'https://www.facebook.com/dialog/feed?'
    params = {
        'app_id': settings.SOCIAL_FB_APP_ID,
        'link': context['page'].full_url,
        'redirect_uri': context['page'].full_url
    }
    return base_url + urlencode(params)


@register.simple_tag(takes_context=True)
def absolutify_static(context, path):
    return context['request'].build_absolute_uri(static(path))


@register.simple_tag(takes_context=True)
def absolutify_media(context, path):
    return context['request'].build_absolute_uri(path)


@register.filter
def replace_space_with_dash(string):
    return string.replace(' ', '-')
