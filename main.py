from graph_complexity import graph
from algorithms.sort import quick_sort
import random

test_cases = []
for i in range(0, 100):
    test_cases.append([random.randint(0,1000) for i in range(random.randint(0,10000))])
results = graph(quick_sort, test_cases, save_file=True)