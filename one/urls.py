from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^begin/', include('login.urls')),
    url(r'^user_home/', include('user_home.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^employees/', include('employees.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^payment', include('payment.urls')),
    ]


if settings.DEBUG:
    settings.MIDDLEWARE+=['one.MiddleWareFix.AtopdedTo110DebugMiddleware']

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
