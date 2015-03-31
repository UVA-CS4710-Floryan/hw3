from negotiator_base import BaseNegotiator
from random import random, shuffle

# Example negotiator implementation, which randomly chooses to accept
# an offer or return with a randomized counteroffer.
# Important things to note: We always set self.offer to be equal to whatever
# we eventually pick as our offer. This is necessary for utility computation.
# Second, note that we ensure that we never accept an offer of "None".
class Negotiator(BaseNegotiator):
    def make_offer(self, offer):
        if random() < 0.05 and offer:
            self.offer = offer
            return offer
        else:
            ordering = self.preferences
            shuffle(ordering)
            self.offer = ordering
            return self.offer
