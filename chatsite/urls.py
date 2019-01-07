
from django.contrib import admin
from django.urls import path
from chatsite import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include("user.urls")),
    path('',views.users.as_view(),name='register'),
    path('login/',views.login_form.as_view(),name='login_form'),
    #path('',include('django.contrib.auth.urls'))
]
urlpatterns=format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns+=(static(settings.STATIC_URL,document_root=settings.STATIC_ROOT))
    #urlpatterns+=(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
