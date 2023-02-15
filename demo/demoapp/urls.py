from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static


urlpatterns = [
    # path('', include('demoapp.url'))
    path('',views.demo,name='demo'),
    # path('about/', views.about, name='about'),
    # path('details/', views.details, name='details'),
    # path('content/', views.content, name='content'),
    # path('credit/', views.credit, name='credit')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)