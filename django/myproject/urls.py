"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Use this for regular Django projects
from django.contrib import admin
# Use this for geospatial projects
#from django.contrib.gis import admin
from django.urls import include, path, re_path

# Import wagtail modules:
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add this to set up authentication for REST framework
    #path('api-auth/', include('rest_framework.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    # wagtail_urls is the base location from where the pages of your Wagtail site will be served.
    # In the above example, Wagtail will handle URLs under /pages/, leaving the root URL and
    # other paths to be handled as normal by your Django project.
    # If you want Wagtail to handle the entire URL space including the root URL,
    # this can be replaced with:
    # re_path(r'', include(wagtail_urls)),
    # ^ In this case, this should be placed at the end of the urlpatterns list,
    # so that it does not override more specific URL patterns.
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URL config goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

w