__author__ = 'zhaoyifei'

from etl.etlimpl.users_etl import UsersEtl

if __name__ == "__main__":
    userEtl = UsersEtl()
    userEtl.execTransform()

# starttime = datetime.datetime.today().timestamp()
# print(starttime)
# userEtl = UsersEtl()
# userEtl.execTransform()
# endtime = datetime.datetime.today().timestamp()
# print(endtime)
# print((int(endtime - starttime)))
