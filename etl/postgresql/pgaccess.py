__author__ = 'zhaoyifei'


import psycopg2
class PgAccess(object):

    def __init__(self, database=None, user=None, password=None, host=None, *, port="6543"):
        # Connect to an existing database
        self.conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    def __enter__(self):
        self.acquire_()
        return self

    def __exit__(self, type, value, traceback):
        self.release_()
        # print("type:", type)
        # print("value:", value)
        # print("trace:", traceback)

    def __del__(self):
        self.conn.close()

    def execFunc(self, func):
        return func(self.cur)

    def execSQL(self, sql, *, params=()):
        print(sql)
        print(params)
        self.cur.execute(sql, params)
        return self.cur.fetchall()

    def execSQLNoResult(self, sql, *, params=()):
        # print(sql)
        self.cur.execute(sql, params)

    def acquire_(self):
        # Open a cursor to perform database operations
        self.cur = self.conn.cursor()

    def release_(self):
        # Make the changes to the database persistent
        self.conn.commit()
        # Close communication with the database
        self.cur.close()

    def execBulk(self, list):

        # self.cur.execute("begin transaction;")
        for tr in list:
            # print(tr)
            # print(len(tr))
            self.cur.execute(tr[0], tr[1])
        # self.cur.execute("commit transaction;")

    def execMany(self, sql, *, paramlist):
        self.cur.executemany(sql, paramlist)

