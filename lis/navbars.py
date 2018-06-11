from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar
from edc_lab_dashboard.dashboard_urls import dashboard_urls as lab_dashboard_urls

lis = Navbar(name='lis')

lis.append_item(
    NavbarItem(
        name='lab',
        label='Specimens',
        fa_icon='fa-flask',
        url_name=lab_dashboard_urls.get('requisition_listboard_url')))

lis.append_item(
    NavbarItem(
        name='sample_reception',
        label='SampleReception',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('sample_reception_listboard_url')))

site_navbars.register(lis)
