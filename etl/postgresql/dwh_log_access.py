__author__ = 'zhaoyifei'

from etl.postgresql import pgaccess
import threading
from etl.tools.config_access import Config
class DwhLog(object):


    def __init__(self):
        Config()
        self.pga = pgaccess.PgAccess(database=Config.pg['database'], user=Config.pg['user'], password=Config.pg['password'], host=Config.pg['host'])
        self.sqlL = list()
        self._lock = threading.Lock()
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._persist_() if len(self.sqlL) >= 1 else print(len(self.sqlL))

    def __del__(self):
        # self._persist_()
        del self.sqlL

    sql = 'INSERT INTO datawarehouse_exec_log(\
            exec_time, mongo_document, exec_item_num, mongo_document_last_item_time)\
            VALUES (%s, %s, %s, %s);'

    def log(self, exec_time, mongo_document, exec_item_num, mongo_document_last_item_time):
        with self._lock:
            self.sqlL.append((self.sql, (exec_time, mongo_document, exec_item_num, mongo_document_last_item_time)))

    def _persist_(self):
        with self._lock:
            with self.pga:
                self.pga.execBulk(self.sqlL)
            del self.sqlL
            self.sqlL = list()

