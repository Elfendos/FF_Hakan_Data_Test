from Methods.Helper import *


def rule2():
    QUERY = (
        'SELECT '
        'pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude FROM '
        '`firefly-330213.FF_March_2014.March_Data` '
        'GROUP BY pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude '
        'HAVING COUNT(pickup_longitude) > 1 ')
    return query_helper(QUERY)
