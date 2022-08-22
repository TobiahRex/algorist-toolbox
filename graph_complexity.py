import time as time
import numpy as np
import matplotlib.pyplot as plot


def graph(*args, **kwargs):
    gc = GraphComplexity()
    return gc.run(*args, **kwargs)

class GraphComplexity:
    def __init__(self):
        self.input_sizes = []
        self.run_times = []

    def run(self, func, test_cases=None, save_file=False, save_path='./plot.png'):
        outputs = self.graph_many(func, test_cases)
        self.plot_results(save_file, save_path)
        return outputs or None

    def graph_many(self, func, test_cases):
        results = []
        for tc in test_cases:
            start_time = time.time()
            self.input_sizes.append(len(tc))
            result = func(tc)
            if result:
                results.append(result)
            total_time = time.time() - start_time
            self.run_times.append(total_time)
        return results or None

    def plot_results(self, save_file, save_path):
        plot.xlabel('Input Size')
        plot.ylabel('Time')
        p = np.poly1d(np.polyfit(self.input_sizes, self.run_times, 5))
        plot.plot(self.input_sizes, self.run_times, 'or')
        plot.plot(self.input_sizes, [p(n) for n in self.input_sizes], '.b')
        plot.show()
        if save_file:
            if '.' in save_path:
                plot.savefig(save_path)

if __name__ == '__main__':
    from algorithms.sort import quick_sort
    import random
    test_cases = []
    for i in range(0, 100):
        test_cases.append([random.randint(0,1000) for i in range(random.randint(0,10000))])
    results = graph(quick_sort, test_cases)
