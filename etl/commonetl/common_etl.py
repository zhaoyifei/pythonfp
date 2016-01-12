__author__ = 'zhaoyifei'

from etl.postgresql import pgaccess
from etl.mongo import mongodbaccess
from pymongo import DESCENDING
from etl.postgresql import dwh_meta_access
from etl.tools.util_ import getNowTimestamp
from etl.postgresql import dwh_log_access
from etl.tools.column_type_transform import timeStampTrans
import abc
import time
from etl.tools.config_access import Config
from functools import wraps
def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

# This is a abstract class
class CommonEtl(metaclass=abc.ABCMeta):
    # @abc.abstractmethod
    # def bulkRead(self, db, func):
    #     pass

    def __init__(self):
        self.config = Config()
    @abc.abstractmethod
    def dealJson(self, item, func):
        pass

    def insertPsq(self, sql, params):
        with pgaccess.PgAccess(database=self.config.pg['database'], user=self.config.pg['user'], password=self.config.pg['password'], host=self.config.pg['host']) as pga:
            pga.execMany(sql, paramlist=params)

    def curryDealJson(self, item):
        return self.dealJson(item, self.insertPsq)

    def curryFunc(self, db):
        return self.bulkRead(db, self.curryDealJson)

    @timethis
    def execTransform(self):
        ma = mongodbaccess.MongoDBAccess(dbname=self.config.mongo['dbname'], host=self.config.mongo['host'])
        ma.execFunc(self.curryFunc)

    def bulkReadTemp(self, documentname, *, max=1000):
        def bulkReadCurry(db, func):
            document = db[documentname]
            dma = dwh_meta_access.DwhMetaData()
            with dma:
                start = dma.getLastTime(documentname)
                end = getNowTimestamp() * 1000

            condition = {'statisticsUpdatedAt': {'$gt': start, '$lt': end}}
            total = document.count(condition)
            print(str(total)+" items data need to be update into datawarehouse!")
            print("start!")
            for i in range(0, int(total/max) + 1):
                userIt = document.find(filter=condition).batch_size(max).skip(i*max).limit(max).sort("createdAt", DESCENDING)
                func(userIt)
                print(str(i+1)+"k items in Pqs!")
            print("success!")
            with dma:
                dma.updateLastTime(documentname, end)
            with dwh_log_access.DwhLog() as dla:
                dla.log(timeStampTrans(end), documentname, total, end)
        self.bulkRead = bulkReadCurry