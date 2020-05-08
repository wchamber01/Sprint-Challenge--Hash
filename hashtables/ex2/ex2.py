#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # initialize cache and flights list
    cache = {}
    flights = list()

    # Loop through tickets list and create cache
    for item in tickets:
        #       key             value
        cache[item.source] = item.destination

    # Set starting point to cache key None (first location)
    origination = cache['NONE']
    # print('origination:', origination)
    # print('cache:', cache)

    # Loop through tickets while the length of route is less than the number of tickets
    while len(flights) < length:

        # Add the originating point to the route list
        flights.append(origination)
        # print('flights:', flights)
        # print('origination:', origination)

        # Make the new origination the originating point's value i.e: destination
        origination = cache[origination]

    return flights
