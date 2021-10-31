from Methods.Helper import *


# All list where there is no passenger but got tip from passenger
def erroneous2():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` where passenger_count = 0 and tip_amount > 0')
    return query_helper(QUERY)
