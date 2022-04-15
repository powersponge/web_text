from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.main, name="main"),
 	path('map/', views.map, name="map"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
