# -*- coding: utf-8 -*-

from collections import namedtuple
from functools import wraps

from dstools.utils.log import get_default_logger


__all__ = (
    'Arg',

    'filter_kwargs',
    'init_parser',
)

Arg = namedtuple('Arg', ['flags', 'dest', 'type', 'choices', 'help', ])

default_logger = get_default_logger()


def init_parser(parser, args, args_defaults, logger=default_logger):
    """ Generate arguments for command line parser(argparse) by preset args and defaults

    Parameters
    ----------
    parser : obj
    args : list
        List of named tupples
    args_defaults : dict
        Map of default values
    logger : logging.logger (optional)
        Logger object

    Returns
    -------
    parser : obj
        Returns updated parser from input
    """
    for arg in args:
        default = args_defaults.get(arg.dest)
        kwargs = {
            'dest': arg.dest,
            'type': arg.type,
            'default': default,
            'help': arg.help.format(default=default),
        }

        if arg.choices: kwargs['choices'] = arg.choices

        parser.add_argument(*arg.flags, **kwargs)

    return parser


def filter_kwargs(ctx='', args_map=None):
    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            logger = kwargs.pop('logger', None)
            _logger = logger or default_logger
            filtered_kwargs = _filter_kwargs(args_map, kwargs, ctx=ctx, logger=_logger)

            if logger:
                filtered_kwargs['logger'] = _logger

            return func(*args, **filtered_kwargs)

        return _wrapper

    return wrapper


def _filter_kwargs(args_map, kwargs, ctx='', logger=default_logger):
    """Filter kwargs by preset iterable.

    Parameters
    ----------
    args_map : iterable
        Collection with allowed arguments name
    kwargs : dict
        Arguments map to filter
    ctx : str (optional)
        Part of debug log message
    logger : logging.Logger (optional)
        Logger object

    Returns
    -------
    filtered_kwargs : dict
        Returns map with allowed arguments
    """
    filtered_kwargs = {}

    if not kwargs:
        return filtered_kwargs

    for k, v in kwargs.iteritems():
        if args_map is None:
            filtered_kwargs[k] = v
            continue
        if k in args_map:
            filtered_kwargs[k] = v
            continue

        if logger:
            logger.debug('(%s) filtered: %s = %s', ctx, k, v)

    return filtered_kwargs
