import functools
import time
from typing import Any, Tuple, Dict, Union

current_time = lambda: int(time.time())
CacheEntry = Dict[str, Union[Any, int]]

def cache(seconds: int):
    def decorator_cache(func):
        @functools.wraps(func)
        def wrapper(
          *args: Tuple[Any], **kwargs: Dict[str, Any]
        ) -> Any:
            if not hasattr(wrapper, 'cache') or wrapper.cache is None:
                wrapper.cache = {}

            key = (args, frozenset(kwargs.items()))
            if key not in wrapper.cache or current_time() - wrapper.cache[key]['time'] > seconds:
                result = func(*args, **kwargs)
                wrapper.cache[key] = {'result': result, 'time': current_time()}
                return result
            else:
                return wrapper.cache[key]['result']

        return wrapper

    return decorator_cache
