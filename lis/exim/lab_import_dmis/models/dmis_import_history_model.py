from lis.core.lock.models import BaseImportHistoryModel


class DmisImportHistoryModel(BaseImportHistoryModel):

    class Meta:
        app_label = 'lab_import_dmis'
