__author__ = 'zhaoyifei'

from etl.tools import column_type_transform
import json

if __name__ == "__main__":
    print(column_type_transform.arrayTrans([12, 232, 334, 42, 532, 236, 17, 218]))
    print(column_type_transform.arrayTrans(['1', '2', '3', '4', '5']))
    print(column_type_transform.arrayTrans(['1a', '2a', '3a', '4a', '5a']))
    print(column_type_transform.arrayTrans(['a', 'a', 'a', 'a', 'a']))
    print(column_type_transform.booleanTrans(True))
    print(column_type_transform.booleanTrans('True'))
    print(column_type_transform.booleanTrans(False))
    print(column_type_transform.booleanTrans('False'))
    print(column_type_transform.booleanTrans('aa'))
    print(column_type_transform.booleanTrans('false'))
    print(column_type_transform.floatTrans(1.2))
    print(column_type_transform.floatTrans(1.0))
    print(column_type_transform.floatTrans(1))
    print(column_type_transform.floatTrans('1.3'))
    print(column_type_transform.floatTrans('1.'))
    print(column_type_transform.floatTrans('.3'))
    print(column_type_transform.floatTrans('d'))
    print(column_type_transform.floatTrans({'a':2}))
    print(column_type_transform.integerTrans(1.0))
    print(column_type_transform.integerTrans(1.3))
    print(column_type_transform.integerTrans(1.9))
    print(column_type_transform.integerTrans(1))
    print(column_type_transform.integerTrans('1'))
    print(column_type_transform.integerTrans('d'))
    print(column_type_transform.integerTrans({'a':2}))
    print(column_type_transform.timeStampTrans(1450500062))
    print(column_type_transform.timeStampTrans('1450500062'))
    print(column_type_transform.timeStampTrans('1450500062130'))

    jsonObj = {'a': 'a', 'b': {'b1': 'b1', 'b2': 'b2'}}
    encodedjson = json.dumps(jsonObj)
    print(column_type_transform.getValueFromJsonRecurs(jsonObj, 'b.b1', str))
