__author__ = 'zhaoyifei'
from etl.etlimpl.doctor_etl import *
from etl.etlimpl.order_etl import *
from etl.etlimpl.reports_etl import *
from etl.etlimpl.users_etl import *
if __name__ == "__main__":
    userEtl = UsersEtl()
    userEtl.execTransform()
    reportEtl = ReportsEtl()
    reportEtl.execTransform()
    doctorEtl = DoctorEtl()
    doctorEtl.execTransform()
    ordersEtl = OrdersEtl()
    ordersEtl.execTransform()

#TODO add lock in postgresql keep that only one process can etl operate datawarehouse at once time.
#TODO dynamic load module to run
