from functools import reduce

class BaseNegotiator:
    # Constructor 
    def __init__(self):
        self.preferences = []
        self.history = []
        self.offer = []

    # Performs per-round initialization - takes in a dictionary of item : utility mappings
    def initialize(self, preferences):
        self.preferences = preferences

    # Given the current utility mapping, the most recently made offer from the other negotiator, 
    # and any other historical data from the current series of negotiations, make a proposed offer
    # To accept an offer, return the same offer as that passed in
    def make_offer(self, offer):
        pass

    # Return the utility given by the last offer - Do not modify this method.
    def utility(self):
        total = len(self.preferences)
        return reduce(lambda points, item: points + ((total / (self.offer.index(item) + 1)) - abs(self.offer.index(item) - self.preferences.index(item))), self.offer, 0)

    # Store the utility the other negotiator received from the last offer
    def receive_utility(self, utility):
        pass

    # Store the results of the last series of negotiation (points won, success, etc.)
    def receive_results(self, results):
        pass
