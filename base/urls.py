from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('blog/', views.blog, name = 'blog'),
    path('show-blog/', views.blogSingle, name = 'blogSingle'),
    path('register/', views.signUp, name = 'signUp'),
    path('profile/', views.profile, name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)