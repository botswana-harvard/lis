import logging
from lis.core.lock.classes import BaseLock
from lis.exim.lab_import_dmis.models import DmisLockModel, DmisImportHistoryModel

logger = logging.getLogger(__name__)


class NullHandler(logging.Handler):
    def emit(self, record):
        pass
nullhandler = logger.addHandler(NullHandler())


class DmisLock(BaseLock):

    def __init__(self, db):
        self.db = db
        super(DmisLock, self).__init__(db, DmisLockModel, DmisImportHistoryModel)
