from django.conf.urls import url , include #include e7na elly benzwedha 34an ne2darn include el apps urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   	url(r'^admin/', admin.site.urls),
	url(r'^cart/', include('cart.urls', namespace="cart")),
	url(r'^photos/' , include('photos.urls',namespace = "shop")),
	url(r'^users/' , include('users.urls', namespace = "users")),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.PHOTOS_URL, document_root=settings.PHOTOS_ROOT)



