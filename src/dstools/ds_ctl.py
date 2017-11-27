# -*- coding: utf-8 -*-

import argparse
import logging
import os

import dstools.tree.dtc as dtc
import dstools.utils.args as args
import dstools.utils.dataset as dataset
import dstools.utils.limits as limits

from dstools.utils.log import (get_default_logger, )


__all__ = (
    'dtc_fit',
)


__version__ = "1.0.4"

DEFAULT_VERBOSE = False
DEFAULT_DRY_RUN = True
DEFAULT_DEMO = False

logger = get_default_logger()


def dtc_fit_processor(
    verbose=DEFAULT_VERBOSE,
    dry_run=DEFAULT_DRY_RUN,
    demo=DEFAULT_DEMO,
    logger=logger,
    **kwargs
):
    """ Entry point for DTC.fit

    Parameters
    ----------
    verbose : bool (optional)
        Enable DEBUG severity for logging
    dry_run : bool (optional)
        Enable Dry-run mode
    demo : bool (optional)
        Enable demo mode (without data loading from input path)
    logger : logging.Logger
        Logger object
    kwargs : dict
        Arguments for DTC and dtc.fit
    """
    if verbose: logger.setLevel(logging.DEBUG)
    if dry_run:
        logger.warning('Dry-run mode is turned ON. Exitting...')
        return

    limits.set_limits(logger=logger, **kwargs)
    X, y = dataset.load(logger=logger, **kwargs) if not demo else [[0, 0], [1, 1]], [0, 1]
    dt_classifier = dtc.fit(X, y, logger=logger, **kwargs)
    dataset.save(dt_classifier, logger=logger, **kwargs)


def _get_default_subparser(subparsers, parser_name):
    parser = subparsers.add_parser(parser_name)

    parser.add_argument(
        '-v', '--verbose',
        dest='verbose',
        action='store_true',
        default=DEFAULT_VERBOSE,
        help='Debug logging level (default: {})'.format(DEFAULT_VERBOSE),
    )

    parser.add_argument(
        '-d', '--demo',
        dest='demo',
        action='store_true',
        default=DEFAULT_DEMO,
        help='Demo test data(without load from input path) (default: {})'.format(not DEFAULT_DEMO),
    )

    parser.add_argument(
        '-D',
        dest='dry_run',
        action='store_false',
        default=DEFAULT_DRY_RUN,
        help='Dry run mode off (default: {})'.format(not DEFAULT_DRY_RUN),
    )

    return parser


def get_dtc_fit_args(subparsers):
    """ Prepare subparser for DTC.fit

        Parameters
        ----------
        subparsers : argparse subparser
    """
    parser = _get_default_subparser(subparsers, 'dtc_fit')

    args.init_parser(parser, limits.ARGS, limits.DEFAULT_KWARGS)
    args.init_parser(parser, dataset.LOAD_ARGS, dataset.DEFAULT_LOAD_KWARGS)
    args.init_parser(parser, dataset.SAVE_ARGS, dataset.DEFAULT_SAVE_KWARGS)
    args.init_parser(parser, dtc.ARGS, dtc.DEFAULT_KWARGS)

    parser.set_defaults(func=dtc_fit_processor)


def parse_args():
    """ Function to prepare argparse parser and parse command line arguments

    Returns
    -------
    args : parsed args
    """
    parser = argparse.ArgumentParser(description='DS CTL (v.%s)' % (__version__, ))
    subparsers = parser.add_subparsers()

    get_dtc_fit_args(subparsers)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    params = vars(args)
    func = params.pop('func')

    func(**params)
