"""sgdonpe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from sgdonpe.core import views as core_views
from sgdonpe.authentication import views as bootcamp_auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', bootcamp_auth_views.signup, name='signup'),
    url(r'^documents/', include('sgdonpe.documents.urls')),
    url(r'^historiers/', include('sgdonpe.historiers.urls',namespace='historiers')),
    #url(r'^remitos/', include('sgdonpe.remitos.urls')),
    url(r'^webservice/', include('sgdonpe.remitos.urls')),
    url(r'^activities/', include('sgdonpe.activities.urls')),
    url(r'^mesadepartes/', include('sgdonpe.mesadepartes.urls')),
]

