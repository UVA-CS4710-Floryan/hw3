from csv import DictReader
from sys import argv, exit
from itertools import islice
from negotiator import Negotiator
from random import seed, randint

def read_scenario(parameterfile_name):
    with open(parameterfile_name, 'r') as parameterfile:
        number_iterations = parameterfile.readline()
        return (
                int(number_iterations),
                list(DictReader(parameterfile, fieldnames=["item_name", "negotiator_a", "negotiator_b"]))
                )

def negotiate(num_iterations, negotiator_a, negotiator_b, a_order, b_order):
    (offer_a, offer_b) = (negotiator_a.make_offer(None), negotiator_b.make_offer(None))
    a_scale = randint(1, 11)
    b_scale = randint(1, 11)
    for i in range(num_iterations):
        print(offer_a, offer_b)
        utility = (a_scale * negotiator_a.utility(), b_scale * negotiator_b.utility())
        negotiator_a.receive_utility(utility)
        negotiator_b.receive_utility(utility)
        if offer_a == offer_b:
            return (True, offer_a, i)
        offer_a = negotiator_a.make_offer(offer_b)
        offer_b = negotiator_b.make_offer(offer_a)

    return (False, None, num_iterations)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please provide at least one scenario file, in csv format.")
        exit(-42)
    score_a = score_b = 0
    negotiator_a = Negotiator()
    negotiator_b = Negotiator()
    for scenario in argv[1:]:
       (num_iters, mapping) = read_scenario(scenario)
       a_mapping = {item["item_name"] : item["negotiator_a"] for item in mapping}
       a_order = sorted(a_mapping, key=a_mapping.get, reverse=True)
       b_mapping = {item["item_name"] : item["negotiator_b"] for item in mapping}
       b_order = sorted(b_mapping, key=b_mapping.get, reverse=True)
       negotiator_a.initialize(a_order)
       negotiator_b.initialize(b_order)
       (result, order, count) = negotiate(num_iters, negotiator_a, negotiator_b, a_order, b_order)
       (points_a, points_b) = (negotiator_a.utility(), negotiator_b.utility()) if result else (-len(a_order), -len(b_order))
       results = (result, points_a, points_b, count)
       score_a += points_a
       score_b += points_b
       negotiator_a.receive_results(results)
       negotiator_b.receive_results(results)
       print("{} negotiation:\n\tNegotiator A: {}\n\tNegotiator B: {}".format("Successful" if result else "Failed", points_a, points_b))
    print("Final result:\n\tNegotiator A: {}\n\tNegotiator B: {}".format(score_a, score_b))
