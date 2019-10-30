import sys
sys.path.append(r'D:\My stuffs\Software Engineering\mysite\mysite')
from django.contrib import admin
from django.urls import path,register_converter, re_path,include
from URLS import views
from URLS import converters
from website.main import views as main_views
from website.page import views as page_views
from credit import views as credit_views
register_converter(converters.FourDigitYearConverter, 'yyyy') #1


extra_patterns = [
    path('reports/', credit_views.report),
    path('reports/<int:id>/', credit_views.report),
    path('charge/', credit_views.charge),
    path('<username>/blog/', include('foo.urls.blog'))
]

urlpatterns = [ # work as Regular expression
    #path('admin/', admin.site.urls),
    #path('articles/2003/', views.special_case_2003), #example
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    #path('articles/<yyyy:year>/',views.year_archive), #1
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive), # alternative way to represent
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$'\
            , views.article_detail),
    re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', views.comments), # good regex
    path('blog/page<int:num>/', views.page),
    path('', main_views.homepage),
    path('credit/', include(extra_patterns)),
    path('<page_slug>-<page_id>/history/', page_views.history),
    path('<page_slug>-<page_id>/edit/', page_views.edit),
    path('<page_slug>-<page_id>/discuss/', page_views.discuss),
    path('<page_slug>-<page_id>/permissions/', page_views.permissions),
    path('blog/', include('inner'), {'blog_id': 3}) # inner here is an inner.py
]
from django.http import HttpResponseRedirect
from django.urls import reverse
"""
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
{# Or with the year in a template context variable: #}
<ul>
{% for yearvar in year_list %}
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
{% endfor %}
</ul>
"""
def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
