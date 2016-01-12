__author__ = 'zhaoyifei'

from bson.json_util import dumps, loads

from etl.etlimpl import users_etl
from etl.mongo import mongodbaccess

if __name__ == "__main__":
    ma = mongodbaccess.MongoDBAccess()
    usetl = users_etl.UsersEtl()

    def dealJson(userIt):
        for u in userIt:
            print(len(usetl.readJson(loads(dumps(u)))))
            # for item in loads(dumps(u)):
                # print(item+": ")
                # print(loads(dumps(u))[item])


    def curryFunc(db):
        return mongodbaccess.bulkReadUser(db, dealJson)

    ma.execFunc(curryFunc)