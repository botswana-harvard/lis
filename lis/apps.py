from datetime import datetime
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig


style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'lis'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP093'
    protocol_name = 'lis'
    protocol_number = '092'
    protocol_title = ''
    study_open_datetime = datetime(
        2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2019, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))


class EdcLabAppConfig(BaseEdcLabAppConfig):
    requisition_model = 'sample_reception.subjectrequisition'
    result_model = 'edc_lab.result'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Lis'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    device_role = CENTRAL_SERVER
    device_id = '99'



class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '093'
