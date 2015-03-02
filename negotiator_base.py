class Negotiator:
    # Constructor 
    def __init__(self):
        self.preferences = None
        self.history = None

    # Performs per-round initialization - takes in a dictionary of item : utility mappings
    def initialize(self, preferences):
        self.preferences = preferences

    # Given the current utility mapping and any other historical data from 
    # the current series of negotiations, make a proposed offer
    def make_offer(self):
        pass

    # Return the utility given by the last offer
    def get_utility(self):
        pass

    # Store the utility the other negotiator received from the last offer
    def receive_utility(self, utility):
        pass

    # Store the results of the last series of negotiation (points won, success, etc.)
    def receive_results(self, results):
        pass
