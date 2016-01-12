__author__ = 'zhaoyifei'

import datetime
import re

# Boolean transform to string
def booleanTrans(b):
    if b == None: return None
    # print(b)
    return 'True' if (isinstance(b, bool) and b is True) or (isinstance(b, str) and b.lower() == 'true') else 'False'

# Number transform to integer
def integerTrans(num):
    if num == None: return -1
    # print(num)
    return int(num) if isinstance(num,(int, float)) or (isinstance(num, str) and re.compile(r'\d*\.d*').match(num)) else 0

def floatTrans(num):
    if num == None: return -1.0
    # print(num)
    return float(num) if isinstance(num,(int, float)) or (isinstance(num, str) and re.compile(r'\d*\.d*').match(num)) else float(0)

def timeStampTrans(time):
    if time == None: return None
    if int(time) < 0:
        return None
    # print(time)
    return datetime.datetime.fromtimestamp(int(time) if int(time) < 10000000000 else int(time)/1000).strftime('%Y-%m-%d %H:%M:%S')

def arrayTrans(l):
    if l == None: return None
    # print(l)
    return "{" + ",".join(map(transStr, l)) + "}"

def transStr(s):
    if s == None: return None
    # print(s)
    return str(s) if isinstance(s, (int, float)) else "\""+str(s)+"\""

def subDocumentArryTrans(key, transFunc):
    def func(json):
        if len(json) > 0:
            return getValueFromJson(json[0], key, transFunc)
        else:
            return None
    return func
    # if 'sub' in json and json['favDoctors'] != None and len(json['favDoctors']) != 0:

def getValueFromJson(json, key, transFunc):
    return transFunc(json[key]) if key in json and json[key] != None else None

def getFromJson(json, key):
    return json[key] if key in json and json[key] != None else None

def getValueFromJsonRecurs(json, key, transFunc):
    if json == None:
        return None
    return getValueFromJson(json, key, transFunc) if key.find('.') == -1 else getValueFromJsonRecurs(getFromJson(json, key.split('.', maxsplit=1)[0]), key.split('.', maxsplit=1)[1], transFunc)

def getTypeFromJson(json, key):
    return type(json[key]) if key in json else None

def timeStampNow():
    return datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
