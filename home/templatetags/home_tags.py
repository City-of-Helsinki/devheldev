import calendar
from django import template
from datetime import date, datetime, timedelta
import pytz
from django.conf import settings
from django.db import connection
from django.db.models import Count
from django.template import defaultfilters
from django.utils.timezone import is_aware, utc
from django.utils.translation import pgettext, ugettext as _, ungettext
from wagtail.wagtailcore.models import Page
from blog.models import BlogPage

register = template.Library()

@register.filter
def first_p(value):
    paras = value.split('</p>')
    if len(paras):
        return paras[0] + '</p>'
    return ''

# settings value
@register.assignment_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('home/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('home/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves all live pages which are children of the calling page
#for standard index listing
@register.inclusion_tag(
    'home/tags/standard_index_listing.html',
    takes_context=True
)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().live()
    return {
        'pages': pages,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.assignment_tag(takes_context=True)
def blog_posts_by_month(context):
    truncate_date = connection.ops.date_trunc_sql('month', 'date')
    qs = BlogPage.objects.extra({'month':truncate_date})
    val = qs.values('month').annotate(Count('pk')).order_by('-month')

    return [{
        'year': x['month'].year,
        'month': x['month'].month,
        'month_name': calendar.month_name[x['month'].month],
        'count': x['pk__count']} for x in val]


@register.assignment_tag
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)


# This filter doesn't require expects_localtime=True because it deals properly
# with both naive and aware datetimes. Therefore avoid the cost of conversion.
@register.filter
def relativetime(value):
    """
    Based on naturaltime. Returns absolute date for times further away,
    relative date and time for times close to present
    """
    if not isinstance(value, date):  # datetime is a subclass of date
        return value

    now = datetime.now(utc if is_aware(value) else None)
    if value < now:
        delta = now - value
        if delta.days != 0:
            return pgettext(
                'naturaltime', '%(delta)s ago'
            ) % {'delta': defaultfilters.timesince(value, now)}
        elif delta.seconds == 0:
            return _('now')
        elif delta.seconds < 60:
            return ungettext(
                # Translators: please keep a non-breaking space (U+00A0)
                # between count and time unit.
                'a second ago', '%(count)s seconds ago', delta.seconds
            ) % {'count': delta.seconds}
        elif delta.seconds // 60 < 60:
            count = delta.seconds // 60
            return ungettext(
                # Translators: please keep a non-breaking space (U+00A0)
                # between count and time unit.
                'a minute ago', '%(count)s minutes ago', count
            ) % {'count': count}
        else:
            count = delta.seconds // 60 // 60
            return ungettext(
                # Translators: please keep a non-breaking space (U+00A0)
                # between count and time unit.
                'an hour ago', '%(count)s hours ago', count
            ) % {'count': count}
    else:
        delta = value - now

        # We must compare the dates in local time
        tz = pytz.timezone(settings.LOCAL_TIME_ZONE)
        now = now.astimezone(tz)
        value = value.astimezone(tz)

        if value.date() == now.date():
            return pgettext(
                'relativetime', 'Today at %(time)s'
            ) % {'time': str(value.strftime('%H:%M'))}
        elif value.date() == (now + timedelta(days=1)).date():
            return pgettext(
                'relativetime', 'Tomorrow at %(time)s'
            ) % {'time': str(value.strftime('%H:%M'))}
        elif value.date() <= (now + timedelta(days=7)).date():
            return pgettext(
                'relativetime', 'Next %(weekday)s at %(time)s'
            ) % {'weekday': str(value.strftime('%A')),
                 'time': str(value.strftime('%H:%M'))}
        else:
            return pgettext(
                'relativetime', '%(date)s at %(time)s'
            ) % {'date': str(value.strftime('%A, %d %B')),
                 'time': str(value.strftime('%H:%M'))}
