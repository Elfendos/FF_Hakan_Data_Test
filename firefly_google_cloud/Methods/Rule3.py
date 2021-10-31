from Methods.Helper import *


def rule3():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` '
        'WHERE '
        'PICKUP_DATETIME < DROPOFF_DATETIME')
    return query_helper(QUERY)
