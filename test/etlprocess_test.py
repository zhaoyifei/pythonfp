__author__ = 'zhaoyifei'

from bson.json_util import dumps, loads

from etl.etlimpl import users_etl
from etl.mongo import mongodbaccess
from etl.postgresql import pgaccess

if __name__ == "__main__":
    ma = mongodbaccess.MongoDBAccess()
    usetl = users_etl.UsersEtl()

    def dealJson(userIt, func):
        sqlList = list()
        for u in userIt:
            sqlList.append((usetl.userSql(), usetl.readJson(loads(dumps(u)))))
        func(sqlList)
            # for item in loads(dumps(u)):
                # print(item+": ")
                # print(loads(dumps(u))[item])

    def insertPsq(sqll):
        with pgaccess.PgAccess() as pga:
            pga.execBulk(sqll)

    def curryDealJson(userIt):
        return dealJson(userIt, insertPsq)

    def curryFunc(db):
        return users_etl.bulkReadUser(db, curryDealJson)

    ma.execFunc(curryFunc)

