__author__ = 'zhaoyifei'

from etl.postgresql import dwh_meta_access

if __name__ == "__main__":
    dma = dwh_meta_access.DwhMetaData()

    with dma:
        print(dma.getLastTime('users'))
        print(dma.updateLastTime('users', 1450667162000))