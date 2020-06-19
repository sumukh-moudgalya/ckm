from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basicapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name='basicapp'

urlpatterns=[
    url(r'^$',views.Baseview.as_view(),name='home_view'),
    url(r'explore/$',views.ExploresListView.as_view(),name='explores_list_view'),
    url(r'explore/(?P<pk>[-\w]+)$',views.ExploresDetailView.as_view(),name='explore_detail'),
    url(r'hotels/$',views.HotelsListView.as_view(),name='hotels_list_view'),
    url(r'hotels/(?P<pk>[-\w]+)$',views.HotelsDetailView.as_view(),name='hotel_detail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
