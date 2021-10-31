from Methods.Helper import *


# Total amount is not equal total
def erroneous3():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` '
        'WHERE '
        'fare_amount + extra + mta_tax + tip_amount + tolls_amount != total_amount')
    return query_helper(QUERY)
