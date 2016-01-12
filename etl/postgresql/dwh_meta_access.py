__author__ = 'zhaoyifei'

from etl.postgresql import pgaccess
import threading
from etl.tools.column_type_transform import timeStampNow
from etl.tools.config_access import Config
class DwhMetaData(object):
    def __init__(self):
        self.config = Config()
        self.pga = pgaccess.PgAccess(database=self.config.pg['database'], user=self.config.pg['user'], password=self.config.pg['password'], host=self.config.pg['host'])
        self._lock = threading.Lock()
        self.__initMap()

    def __initMap(self):


        self.selectSql = "SELECT id, mongo_document_name, last_update_time, execute_time\
          FROM datawarehouse_timestamp_meta where mongo_document_name=%s; "
        self.updateSql = "UPDATE datawarehouse_timestamp_meta\
          SET last_update_time=%s, execute_time=%s\
          WHERE mongo_document_name=%s;"
        self.insertSql = "INSERT INTO datawarehouse_timestamp_meta(\
            mongo_document_name, last_update_time, execute_time)\
            VALUES (%s, %s, %s);"

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print(value)
    def __del__(self):
        del self.config

    def getLastTime(self, documentName):
        with self.pga:
            result = self.pga.execSQL(self.selectSql, params=(documentName,))
            if len(result) == 0:
                self.pga.execSQLNoResult(self.insertSql, params=(documentName, 0, timeStampNow()))
                result = self.pga.execSQL(self.selectSql, params=(documentName,))
            return result[0][2]
    def updateLastTime(self, documentName, last_update_time):
        with self.pga:
            self.pga.execSQLNoResult(self.updateSql, params=(last_update_time, timeStampNow(), documentName))




