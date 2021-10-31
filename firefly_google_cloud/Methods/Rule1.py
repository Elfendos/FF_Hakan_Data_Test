from Methods.Helper import *


def rule1():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` '
        'WHERE'
        '(date_diff(pickup_datetime, dropoff_datetime, hour) = 0) and'
        '(date_diff(pickup_datetime, dropoff_datetime, minute) = 0) and'
        '(date_diff(pickup_datetime, dropoff_datetime, second) < 10) and'
        '(pickup_longitude = 0 or pickup_latitude = 0 or dropoff_longitude = 0 or dropoff_latitude = 0)')
    return query_helper(QUERY)
