from django.conf.urls import url

from sgdonpe.activities import views
urlpatterns = [
    #url(r'^$', documents_views.documents, name='documents'),
    #url(r'^post/$', views.post, name='post'),
    #url(r'^like/$', views.like, name='like'),
    #url(r'^comment/$', views.comment, name='comment'),
    #url(r'^load/$', views.load, name='load'),
    #url(r'^check/$', views.check, name='check'),
    #url(r'^load_new/$', views.load_new, name='load_new'),
    #url(r'^update/$', views.update, name='update'),
    #url(r'^track_comments/$', views.track_comments, name='track_comments'),
    #url(r'^remove/$', views.remove, name='remove_feed'),
    #url(r'^(?P<idDocument>\d+)/$', historier_views.documentHistory, name='history'),
    #url(r'^addHistory/(?P<idDocument>\d+)/$', historier_views.addHistory, name='historyAdded'),
    #url(r'^updatePrincipalState/(?P<idDocument>\d+)/$', historier_views.agregarActividad, name='historyAdded'),
    url(r'^sendFile/(?P<idDocument>\d+)/$', views.sendFile, name='sendFile'),
    url(r'^addReference/(?P<idDocument>\d+)/$', views.addReference, name='addReference'),

]
