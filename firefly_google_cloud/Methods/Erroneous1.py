from Methods.Helper import *


# Total amount = 0 and trip distance  > 1
def erroneous1():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` where total_amount = 0 and trip_distance > 1')
    return query_helper(QUERY)
