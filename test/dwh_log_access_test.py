__author__ = 'zhaoyifei'

from etl.postgresql import dwh_log_access
from etl.tools.column_type_transform import timeStampTrans

if __name__ == "__main__":
    dla = dwh_log_access.DwhLog()
    with dla:
        for i in range(0, 9):
            dla.log(timeStampTrans(1450667162), 'users', 30, 1450667162000)
    with dla:
        dla.log(timeStampTrans(1450667162), 'users', 30, 1450667162000)
