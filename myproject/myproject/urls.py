"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from digi2corp.views import contact_view , signup_view, profile_view, signin_view, upload_view, upload_resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('services', TemplateView.as_view(template_name='services.html'), name='services'),
    path('contact', contact_view, name='contact'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('team', TemplateView.as_view(template_name='team.html'), name='team'),
    path('profile', profile_view, name='profile'),
    path('signup', signup_view, name='signup'),
    path('signin', signin_view, name='signin'),
    path('joblist',TemplateView.as_view(template_name='job_list.html'), name='joblist'),
    # path('upload_cv',TemplateView.as_view(template_name='upload_cv.html'), name='upload_cv'),
    path('upload_cv', upload_view, name='upload_cv'),
    path('upload', upload_resume, name='upload_resume'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
