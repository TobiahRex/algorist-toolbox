from algorithms.sort import quick_sort
from graph_complexity import graph, graph_many
import random


@graph
def fun1(arr):
    return quick_sort(arr)

@graph_many
def fun2(arr):
    return quick_sort(arr)


def _get_test_cases():
    ten_test_cases = []
    for _ in range(0, 10):
        ten_test_cases.append([random.randint(0,1000) for i in range(random.randint(0,10000))])
    return ten_test_cases

def example_1():
    """ Run like normal.
    A single test result will be graphed and shown in a popup.
    """
    for test_case in _get_test_cases():
        result = fun1(test_case)
        print(result)

def example_2():
    """ Run your function by explicitly calling the attached `.run()` method with your test case.
    - All test results will be saved for you "under the hood", ready to be called.
    - Call the `.results()` method to receive your results in the order called.
    """
    for test_case in _get_test_cases():
        fun2.run(test_case)
    results = fun2.results()

def example_3():
    """Run your function & plot the results of all your results.
    - A popup will appear with all your results from all your tests in a single graph.
    - If you call `.plot()` first, you can chain with `.results()` after.
    """
    for test_case in _get_test_cases():
        fun2.run(test_case)
    results = fun2 \
        .plot() \
        .results()

def example_4():
    """Run your function & plot & save the results to a local file.
    You can also customize the file name & location.
    """
    for test_case in _get_test_cases():
        fun2.run(test_case)
    results = fun2 \
        .plot(save_file=True, filename='./my_file.png') \
        .results()


if __name__ == '__main__':
    [m() for m in [
        example_1,
        example_2,
        example_3,
        example_4,
    ]]