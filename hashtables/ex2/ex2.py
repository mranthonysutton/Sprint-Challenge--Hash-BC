#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Loop through each ticket and grab the source and destination
    # Add the source & destination to the hashtable

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Sets the default HashTable index to 0
    index = 0

    current_index = hash_table_retrieve(hashtable, "NONE")

    # Goes through the hashtable and sets the current_ticket to the current index and returns the routes
    while index < len(route):
        route[index] = current_index
        index += 1

        current_index = hash_table_retrieve(hashtable, current_index)

    return route[:-1]
