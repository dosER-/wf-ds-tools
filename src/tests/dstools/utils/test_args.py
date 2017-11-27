# -*- coding: utf-8 -*-

import unittest

from  dstools.utils.args import (Arg, _filter_kwargs, )


class TestArgs(unittest.TestCase):

    def test_filter_kwargs_extra(self):
        args = [
            Arg(
                flags=['-k1', '--k1-long'],
                dest='k1', type=str, choices=None,
                help='Help (default: {default})'
            ),
            Arg(
                flags=['-k2', '--k2-long'],
                dest='k2', type=str, choices=None,
                help='Help (default: {default})'
            ),
            Arg(
                flags=['-k3', '--k3-long'],
                dest='k3', type=str, choices=None,
                help='Help (default: {default})'
            ),
        ]
        args_map = {a.dest: a for a in args}

        input_kwargs = {'k1': 'kv1', 'k2': 'kv2', 'k3': 'kv3', 'f1': 'fv1', 'f2': 'fv2'}
        expected = {'k1': 'kv1', 'k2': 'kv2', 'k3': 'kv3'}
        output = _filter_kwargs(args_map, input_kwargs, logger=None)

        self.assertEqual(expected, output)

    def test_filter_kwargs_low(self):
        args = [
            Arg(
                flags=['-k1', '--k1-long'],
                dest='k1', type=str, choices=None,
                help='Help (default: {default})'
            ),
            Arg(
                flags=['-k2', '--k2-long'],
                dest='k2', type=str, choices=None,
                help='Help (default: {default})'
            ),
            Arg(
                flags=['-k3', '--k3-long'],
                dest='k3', type=str, choices=None,
                help='Help (default: {default})'
            ),
        ]
        args_map = {a.dest: a for a in args}

        input_kwargs = {'k1': 'kv1', 'k2': 'kv2'}
        expected = {'k1': 'kv1', 'k2': 'kv2'}
        output = _filter_kwargs(args_map, input_kwargs, logger=None)

        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
