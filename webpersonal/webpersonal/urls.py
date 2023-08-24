"""
URL configuration for webpersonal project.

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
from django.urls import path
from core import views as core_views

from django.conf import settings

urlpatterns = [
    path('', core_views.principal, name="principal"),
    path('nosotros/', core_views.nosotros, name="nosotros"),
    path("admin/", admin.site.urls),
    path('contacto/', core_views.contacto, name="contacto"),
    path('productos/', core_views.productos, name="productos"),
    path('refrigeradora/<int:refrigeradora_id>', core_views.refrigeradora, name="refrigeradora"),
    path('microonda/<int:microonda_id>', core_views.microondas, name="microonda"),
    path('lavadora/<int:lavadora_id>', core_views.lavadora, name="lavadora"),
    path('televisor/<int:televisor_id>', core_views.televisor, name="televisor"),
    path('licuadora/<int:licuadora_id>', core_views.licuadora, name="licuadora"),
    path('cocina/<int:cocina_id>', core_views.cocina, name="cocina")
]




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
