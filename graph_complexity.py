import time as time
import numpy as np
import matplotlib.pyplot as plot


def graph(func):
    gc = GraphComplexity()
    def wrapper(*args, **kwargs):
        gc.run(func, *args, **kwargs)
        return gc.results()[0]
    return wrapper

def graph_many(func):
    gc = GraphComplexity()
    def wrapper(*args, **kwargs):
        return gc
    return wrapper

class GraphComplexity:
    def __init__(self):
        self.__input_sizes = []
        self.__run_times = []
        self.__results = []

    def run(self, func, test_case, show_time=False):
        self.__run_tests(func, test_case, show_time)

    def __run_tests(self, func, test, show_time):
        start_time = time.time()
        self.__input_sizes.append(len(test))
        result = func(test)
        if result:
            self.__results.append(result)
        total_time = time.time() - start_time
        if show_time:
            print(total_time)
        self.__run_times.append(total_time)

    def results(self):
        return self.__results

    def plot(self, save_file=False, save_path='./plot.png'):
        if not (self.__input_sizes and self.__run_times):
            print('GraphComplexity: No test results to plot.')
            return None
        plot.xlabel('Input Size')
        plot.ylabel('Time')
        p = np.poly1d(np.polyfit(self.__input_sizes, self.__run_times, 5))
        plot.plot(self.__input_sizes, self.__run_times, 'or')
        plot.plot(self.__input_sizes, [p(n) for n in self.__input_sizes], '.b')
        plot.show()
        if save_file:
            if '.' in save_path:
                plot.savefig(save_path)
        return self


if __name__ == '__main__':
    @graph
    def fun(n):
        if n > 0:
            print('n: ', n)
            fun(n - 1)
        return