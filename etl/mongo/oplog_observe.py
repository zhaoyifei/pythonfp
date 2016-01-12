__author__ = 'zhaoyifei'

import datetime
import traceback

from bson.timestamp import Timestamp
from pymongo.errors import AutoReconnect


# ts：8字节的时间戳，由4字节unix timestamp + 4字节自增计数表示。这个值很重要，在选举(如master宕机时)新primary时，会选择ts最大的那个secondary作为新primary。
# op：1字节的操作类型，例如i表示insert，d表示delete。
# ns：操作所在的namespace。
# o：操作所对应的document,即当前操作的内容（比如更新操作时要更新的的字段和值）
# o2: 在执行更新操作时的where条件，仅限于update时才有该属性

# "i"： insert
# "u"： update
# "d"： delete
# "c"： db cmd
# "db"：声明当前数据库 (其中ns 被设置成为=>数据库名称+ '.')
# "n":  no op,即空操作，其会定期执行以确保时效性


# 当使用复制集(Replica sets)模式时，其会使用下面的local数据库：
#
# local.system.replset 用于复制集配置对象存储 (通过shell下的rs.conf()或直接查询)
# local.oplog.rs       一个capped collection集合.可在命令行下使用--oplogSize 选项设置该集合大小尺寸.
# local.replset.minvalid  通常在复制集内使用，用于跟踪同步状态(sync status)


 unixtime = datetime.datetime(2015, 12, 17, 12).timestamp()
    print(unixtime)
    date = Timestamp(int(unixtime), 1)

    query = {}#{'ts': {'$gt': date}}
    opresult = localdb['oplog.rs'].find(query)  #, cursor_type=CursorType.TAILABLE, oplog_replay=True
    # opresult.add_option(_QUERY_OPTIONS['oplog_replay'])
    # print(localdb['oplog.rs'].count(query))
    print(opresult.alive)
    try:
        while opresult.alive:
            try:
                 doc = opresult.next()
                 print(doc)
            except (AutoReconnect, StopIteration):
                # sleep(_SLEEP)
                traceback.print_exc()
    finally:
        opresult.close()
