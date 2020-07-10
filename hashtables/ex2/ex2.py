#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    flights = {}
    for ticket in tickets:
        if ticket.source == 'NONE':
            route[0] = ticket.destination
        flights[ticket.source] = ticket.destination

    for index in range(1, length):
        source = route[index-1]
        route[index] = flights[source]

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))
