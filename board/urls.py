from django.conf.urls import url
from board import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<school_id>\d+)/$', views.detail, name='detail'),
]
