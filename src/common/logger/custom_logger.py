import functools

import structlog


def get_logger(name: str = ""):
    return structlog.get_logger(name)


def execute_log(logger):
    def _execute_log(f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            logger.debug(f"{f.__module__}.{f.__name__} start")
            ret = f(*args, **kwargs)
            logger.debug(f"{f.__module__}.{f.__name__} finish")
            return ret

        return func

    return _execute_log
