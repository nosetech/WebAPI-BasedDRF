from django.http import HttpResponse

from common.logger import custom_logger

logger = custom_logger.get_logger(__name__)


def index(request):
    sample_func()
    logger.debug(sample_func.__name__)
    return HttpResponse("Hello, world. You're at the polls index.")


@custom_logger.execute_log(logger)
def sample_func():
    logger.debug("test")
