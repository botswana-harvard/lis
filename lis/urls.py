from sample_reception.admin_site import sample_reception_admin
from django.contrib import admin
from django.urls.conf import path, include
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin

from .views import HomeView, AdministrationView

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    path('admin/', admin.site.urls),
    path('admin/', sample_reception_admin.urls),
    path('admin/', edc_lab_admin.urls),
    path('admin/', edc_identifier_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('sample_reception/', include('sample_reception.urls')),
    path('lis/', include('lis_dashboard.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_lab/', include('edc_lab.urls')),
    path('edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_identifier/', include('edc_identifier.urls')),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]
