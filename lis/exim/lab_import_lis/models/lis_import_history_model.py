from lis.core.lock.models import BaseImportHistoryModel


class LisImportHistoryModel(BaseImportHistoryModel):

    class Meta:
        app_label = 'lab_import_lis'
