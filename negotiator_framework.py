from csv import DictReader
from sys import argv
from itertools import islice
from negotiator import Negotiator

def read_scenario(parameterfile_name):
    with open(parameterfile_name, 'r') as parameterfile:
        number_iterations = parameterfile.readline()
        thresholds_a = islice(parameterfile, 2)
        thresholds_b = islice(parameterfile, 2)
        return (
                int(number_iterations),
                tuple(map(int, thresholds_a)), 
                tuple(map(int, thresholds_b)),
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
       (num_iters, thresh_a, thresh_b, mapping) = read_scenario(scenario)
       negotiator_a.initialize({item["item_name"] : item["negotiator_a"] for item in mapping})
       negotiator_b.initialize({item["item_name"] : item["negotiator_b"] for item in mapping})
       (result, count) = negotiate(num_iters, negotiator_a, negotiator_b)
       points_a = points_b = 0
       if result:
           points_a = num_iters - count if thresh_a[0] <= count <= thresh_a[1] else 0
           points_b = num_iters - count if thresh_b[0] <= count <= thresh_b[1] else 0
       results = (result, points_a, points_b, count)
       negotiator_a.receive_results(results)
       negotiator_b.receive_results(results)
    print("Negotiator A: {}\nNegotiator B:{}".format(score_a, score_b))
