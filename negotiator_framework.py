from csv import DictReader
from sys import argv
from itertools import islice
from negotiator import Negotiator

def read_scenario(parameterfile_name):
    with open(parameterfile_name, 'r') as parameterfile:
        number_iterations = parameterfile.readline()
        return (
                int(number_iterations),
                list(DictReader(parameterfile, fieldnames=["item_name", "negotiator_a", "negotiator_b"]))
                )

def negotiate(num_iterations, negotiator_a, negotiator_b):
    offer_a = offer_b = None
    for i in range(num_iterations):
        offer_a = negotiator_a.make_offer(offer_b)
        offer_b = negotiator_b.make_offer(offer_a)
        if offer_a == offer_b:
            return (True, i)
        negotiator_a.receive_utility(negotiator_b.get_utility())
        negotiator_b.receive_utility(negotiator_a.get_utility())
    return (False, num_iterations)

if __id__ == "__main__":
    score_a = score_b = 0
    negotiator_a = Negotiator()
    negotiator_b = Negotiator()
    for scenario in argv:
       (num_iters, mapping) = read_scenario(scenario)
       a_mapping = {item["item_name"] : item["negotiator_a"] for item in mapping}
       a_order = sorted(a_mapping, key=a_mapping.get, reverse=True)
       b_mapping = {item["item_name"] : item["negotiator_b"] for item in mapping}
       b_order = sorted(b_mapping, key=b_mapping.get, reverse=True)
       negotiator_a.initialize(a_mapping)
       negotiator_b.initialize(b_mapping)
       (result, count) = negotiate(num_iters, negotiator_a, negotiator_b)
       total = len(a_order)
       points_a = reduce(lambda points, item: points + ((total / (a_order.index(item) + 1)) - abs(a_order.index(item) - result.index(item))), 0)
       points_b = reduce(lambda points, item: points + ((total / (b_order.index(item) + 1)) - abs(b_order.index(item) - result.index(item))), 0)
       results = (result, points_a, points_b, count)
       score_a += points_a
       score_b += points_b
       negotiator_a.receive_results(results)
       negotiator_b.receive_results(results)
    print("Negotiator A: {}\nNegotiator B:{}".format(score_a, score_b))
