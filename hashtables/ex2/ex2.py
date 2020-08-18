#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dict={}
    route = [None] * length

    for ticket in tickets:
        dict[ticket.source] = ticket.destination
        
    next_flight = dict["NONE"]
    
    for index in range(length):
        route[index] = next_flight
        next_flight=dict[next_flight]

    return route
