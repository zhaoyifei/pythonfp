__author__ = 'zhaoyifei'

from pymongo import MongoClient
# 'mongodb://localhost:27017/'

class MongoDBAccess(object):

    _TAIL_OPTS = {'tailable': True, 'await_data': True}
    _SLEEP = 10


    __DB_HOST = 'localhost'
    __DB_PORT = 27017

    def __init__(self, *, host='localhost', port=27017, dbname='zlyweb'):
        # Connect to an existing database

        self.__client = MongoClient(host, port)
        # print(self.__client.is_locked)
        # print(self.__client.server_info())
        # print(self.__client.is_primary)
        # print(self.__client.is_mongos)
        self.__db = self.__client[dbname]
        self.__localdb = self.__client['local']

    def __del__(self):
        self.__client.close();

    def execFunc(self, func):
        return func(self.__db)

# def bulkReadUser(db, func):
#         user = db['users']
#         max = 500
#         condition = {'createdAt': {'$gt': 1449849600000}}
#         total = user.count(condition)
#         print(total)
#         for i in range(0, int(total/1000) + 1):
#             userIt = user.find(filter=condition).batch_size(max).skip(i*max).limit(max).sort("createdAt", DESCENDING)
#             func(userIt)


