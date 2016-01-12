__author__ = 'zhaoyifei'

import configparser
import os

class Config(object):
    mongo = {}
    pg = {}
    def __init__(self):
        if Config.mongo == {} or Config.pg =={}:
            config = configparser.ConfigParser()
            config.read('config.ini')

            Config.pg['database'] = config.get("postgresql", "database")
            Config.pg['user'] = config.get("postgresql", "user")
            Config.pg['password'] = config.get("postgresql", "password")
            Config.pg['host'] = config.get("postgresql", "host")

            Config.mongo['dbname'] = config.get("mongodb", "dbname")
            Config.mongo['host'] = config.get("mongodb", "host")

    def getPwd(self):
        return os.getcwd()
