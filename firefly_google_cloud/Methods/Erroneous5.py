from Methods.Helper import *


# Geo location entered incorrectly
def erroneous5():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` ' 
        'WHERE ' 
        'pickup_latitude = 0 or dropoff_longitude = 0')
    return query_helper(QUERY)
