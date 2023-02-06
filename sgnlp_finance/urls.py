from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.urls import path, include
from django.conf import settings 

# To be added 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sgnlp_finance_app.urls')),
    # path('engine/', include('app_2.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

print(urlpatterns)
# Add static file urls 
# urlpatterns += staticfiles_urlpatterns()
