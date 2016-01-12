__author__ = 'zhaoyifei'

import datetime

def getNowTimestamp():
    return datetime.datetime.today().timestamp()

def getNowFormat():
    return datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
