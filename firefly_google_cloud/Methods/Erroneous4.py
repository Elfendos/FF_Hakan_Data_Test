from Methods.Helper import *


# Passenger count should not be more then 5 if we consider normal taxi
def erroneous4():
    QUERY = (
        'SELECT * FROM `firefly-330213.FF_March_2014.March_Data` '
        'WHERE '
        'passenger_count > 5')
    return query_helper(QUERY)
