# -*- coding: utf-8 -*-

import resource

from dstools.utils.args import (Arg, filter_kwargs, )
from dstools.utils.log import (get_default_logger, )


__all__ = (
    'ARGS',
    'DEFAULT_KWARGS',

    'set_limits',
)


ARGS = [
    Arg(
        flags=['-cpu', '--max-cpu-seconds'],
        dest='max_cpu_seconds', type=float, choices=None,
        help='Max used CPU seconds (default: {default} (-1: INF))'
    ),
    Arg(
        flags=['-rss', '--max-rss'],
        dest='max_rss', type=int, choices=None,
        help='Max used rss memory in MB (default: {default}MB, (-1: INF))'
    ),
]
ARGS_MAP = {arg.dest: arg for arg in ARGS}
DEFAULT_KWARGS = {
    'max_cpu_seconds': None,
    'max_heap': None,
    'max_rss': None,
    'max_stack': None,
}


logger = get_default_logger()


@filter_kwargs(ctx='limits.set_limits', args_map=ARGS_MAP)
def set_limits(
    max_cpu_seconds=DEFAULT_KWARGS.get('max_cpu_seconds'),
    max_heap=DEFAULT_KWARGS.get('max_heap'),
    max_rss=DEFAULT_KWARGS.get('max_rss'),
    max_stack=DEFAULT_KWARGS.get('max_stack'),
    logger=logger,
):
    """ Set recourse limits

    Parameters
    ----------

    max_cpu_seconds : int (optional)
        Limit of cpu time in seconds
    max_heap : int (optional)
        Limit of memory for data in megabytes
    max_rss : int (optional)
        Limit of resident memory in megabytes
    max_stack : int (optional)
        Limit of stack memoty in megabytes
    logger : logging.Logger (optional)
        Logger object
    """
    _set_resource_limit('cpu', resource.RLIMIT_CPU, max_cpu_seconds, logger=logger)
    _set_resource_limit('heap', resource.RLIMIT_DATA, max_heap, scale=1024, logger=logger)
    _set_resource_limit('rss', resource.RLIMIT_RSS, max_rss, scale=1024, logger=logger)
    _set_resource_limit('stack', resource.RLIMIT_STACK, max_stack, scale=1024, logger=logger)


def _set_resource_limit(name, res_type, res_limit, scale=1, logger=logger):
    if res_limit is None: return
    if res_limit < 0: res_limit = resource.RLIM_INFINITY
    if res_limit != resource.RLIM_INFINITY: res_limit *= scale

    soft, hard = resource.getrlimit(res_type)
    logger.debug('Change resource_limit. type: %s, from: %s, to: %s', name, (soft, hard, ), (res_limit, res_limit))
    resource.setrlimit(res_type, (res_limit, res_limit))
