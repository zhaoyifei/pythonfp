__author__ = 'zhaoyifei'

from etl.postgresql import pgaccess
from etl.tools.column_type_transform import booleanTrans, integerTrans, timeStampTrans, floatTrans, arrayTrans

if __name__ == "__main__":
    def selectLog(cur):
        cur.execute("SELECT count(*) FROM log;")
        rows = cur.fetchall()        # all rows in table
        for row in rows:
            print(row)

    with pgaccess.PgAccess() as pga:
        pga.execFunc(selectLog)

    insertSql = 'INSERT INTO test(\
                m_id, price, birthday, "isDeletec", num, flo, tags, ints)\
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'

    sqlL = []
    print(arrayTrans([123, 34, 43, 54, 12]))
    sqlL.append((insertSql, (None, str('1,000,000'),
                            timeStampTrans(1450576800), booleanTrans(False),
                            integerTrans(12), None,
                            arrayTrans(['ad', 'dfd', 'dfs', 'fsd', 'ewrew']),
                            arrayTrans([123, 34, 43, 54, 12])
                            )
                 )
                )

    sqlL.append((insertSql, (str('dfd'), None,
                            timeStampTrans(1450576800), booleanTrans(False),
                            integerTrans(12), floatTrans(1.23455),
                            arrayTrans(['ad', 'dfd', 'dfs', 'fsd', 'ewrew']),
                            None
                            )
                 )
                )
    sqlL.append((insertSql, (str('dfd'), str('1,000,000'),
                            None, booleanTrans(False),
                            integerTrans(12), floatTrans(1.23455),
                            arrayTrans(['ad', 'dfd', 'dfs', 'fsd', 'ewrew']),
                            arrayTrans([123, 34, 43, 54, 12])
                            )
                 )
                )
    sqlL.append((insertSql, (str('dfd'), str('1,000,000'),
                            timeStampTrans(1450576800), None,
                            integerTrans(12), floatTrans(1.23455),
                            arrayTrans(['ad', 'dfd', 'dfs', 'fsd', 'ewrew']),
                            arrayTrans([123, 34, 43, 54, 12])
                            )
                 )
                )
    sqlL.append((insertSql, (str('dfd'), str('1,000,000'),
                            timeStampTrans(1450576800), booleanTrans(False),
                            None, floatTrans(1.23455),
                            arrayTrans(['ad', 'dfd', 'dfs', 'fsd', 'ewrew']),
                            arrayTrans([123, 34, 43, 54, 12])
                            )
                 )
                )
    sqlL.append((insertSql, (str('dfd'), str('1,000,000'),
                            timeStampTrans(1450576800), booleanTrans(False),
                            integerTrans(12), floatTrans(1.23455),
                            None,
                            arrayTrans([123, 34, 43, 54, 12])
                            )
                 )
                )

    with pgaccess.PgAccess() as pga:
        pga.execBulk(sqlL)
