from functools import cache
import sys
import types
from typing import Any, List, Set, Dict, Tuple
import heapq
import bisect
from sortedcontainers import SortedList, SortedSet, SortedDict


class Solution:
    def beautifulProblem(self, squares: List[List[int]]) -> float:
        raise NotImplementedError
    

"""Notes

If you need to take some notes while implementing the solution, you can write them here.
"""


TEST_CASES: List[Any] = [
    """
    Just copy and paste test cases like so. Make sure each test case is separated by a comma.

    [[0,0,1],[2,2,1]],
    [[0,0,2],[1,1,1]]
    """
]


if __name__ == "__main__":
    solution = Solution()
    
    # Retrieve public Solution method
    method = next((
        getattr(Solution, func)
        for func in dir(Solution)
        if not func.startswith("_") and isinstance(getattr(Solution, func), types.FunctionType
    )))

    # Get number of arguments the method takes
    num_args = method.__code__.co_argcount - 1  # Subtract 1 for 'self'

    # Split test cases into groups based on number of arguments
    grouped_test_cases = [
        TEST_CASES[i:i + num_args]
        for i in range(0, len(TEST_CASES), num_args)
    ]

    for test_case_group in grouped_test_cases:
        result = method(solution, *test_case_group)
        print(f"Input: {test_case_group} => Output: {result}")
