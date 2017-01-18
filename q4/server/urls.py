from django.conf.urls import url 
from server import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    url(r'^$', views.server_index)
]

