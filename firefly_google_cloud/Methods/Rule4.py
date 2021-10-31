from Methods.Helper import *

# Below values are considered as given coordinates.
def rule4():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` '
        'WHERE '
        '(pickup_longitude BETWEEN  -73.96240234375 and 40.743282318115234) AND '
        '(pickup_latitude BETWEEN  40.743282318115234 and -73.96240234375)')
    return query_helper(QUERY)