"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.static import serve

"""
@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)
"""
admin.site.site_header = 'SACEMA Administration Dashboard'
admin.site.site_title = 'SACEMA Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('peoplemanager.urls')),
    path('', include('contactus.urls')),
    # path('', include('archivesuploads.urls')),
    path('', include('newsandevents.urls')),
    path('', include('polls.urls')),
    path('', include('cms.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
