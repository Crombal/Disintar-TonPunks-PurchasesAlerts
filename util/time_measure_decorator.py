# !/usr/bin/env python
"""Script for measure execution time of function."""
import sys
import time
from functools import wraps
from typing import Any, Callable, Dict, Tuple, TypeVar

from loguru import logger


logger.add(sys.stdout, format='{time} {level} {message}', filter='my_module', level='INFO')

RT = TypeVar('RT')


def timeit(func: Callable[..., RT]) -> Callable[..., RT]:
    """
    Measure execution time of function.

    :param func: a callable for measuring time of execution
    :type func: Callable[..., RT]
    :return: wrapped function with calculated execution time of it
    :rtype: Callable[..., RT]
    """
    @wraps(func)
    def timeit_wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> RT:  # noqa: WPS430
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        logger.info(f'Function "{func.__name__}" Took {total_time:.9f} seconds')
        return result

    return timeit_wrapper
