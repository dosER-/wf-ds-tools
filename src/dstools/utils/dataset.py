# -*- coding: utf-8 -*-

import codecs
import os
import pickle

from sklearn.datasets import load_files

from dstools.utils.args import (Arg, filter_kwargs, )
from dstools.utils.log import (get_default_logger, )


__all__ = (
    'LOAD_ARGS',
    'DEFAULT_LOAD_KWARGS',
    'SAVE_ARGS',
    'DEFAULT_SAVE_KWARGS',

    'load',
    'save',
)


LOAD_ARGS = [
    Arg(
        flags=['-ip', '--input-path'],
        dest='input_path', type=str, choices=None,
        help='Path to container directory (default: {default})'
    ),
]
LOAD_ARGS_MAP = {arg.dest: arg for arg in LOAD_ARGS}
DEFAULT_LOAD_KWARGS = {
    'input_path': '~/input',
}

SAVE_ARGS = [
    Arg(
        flags=['-op', '--output-path'],
        dest='output_path', type=str, choices=None,
        help='Path to output file (default: {default})'
    ),
]
SAVE_ARGS_MAP = {arg.dest: arg for arg in SAVE_ARGS}
DEFAULT_SAVE_KWARGS = {
    'output_path': '~/output/data.pickle',
}

logger = get_default_logger()


@filter_kwargs(ctx='dataset.load', args_map=LOAD_ARGS_MAP)
def load(input_path=DEFAULT_LOAD_KWARGS.get('input_path'), logger=logger):
    """Load text files with categories as subfolder names.

    Individual samples are assumed to be files stored a two levels folder
    structure such as the following:

        container_folder/
            category_1_folder/
                file_1.txt
                file_2.txt
                ...
                file_42.txt
            category_2_folder/
                file_43.txt
                file_44.txt
                ...

    The folder names are used as supervised signal label names. The individual
    file names are not important.

    Parameters
    ----------
    input_path : string or unicode
        Path to the main folder holding one subfolder per category
    logger : logging.Logger
        Logger object

    Returns
    -------
    (data, target) : tupple
        data:  the raw text data to learn
        target: the classification labels (integer index)
    """
    input_path = os.path.expanduser(input_path)
    logger.info('Loading data: %s', input_path)

    loaded = load_files(input_path, encoding='utf-8')

    return loaded.data, loaded.target


@filter_kwargs(ctx='dataset.save', args_map=SAVE_ARGS_MAP)
def save(data, output_path=DEFAULT_SAVE_KWARGS.get('output_path'), logger=logger):
    """Pickle and save data to output path

    Parameters
    ----------
    data : object
        Data to save. It must be serializable.
    output_path : string or unicode
        Path to the output file
    logger : logging.Logger
        Logger object

    Returns
    -------
    """
    output_path = os.path.expanduser(output_path)
    logger.info('Saving data: %s', output_path)

    if not data: return

    logger.debug('Making dirs...')
    os.umask(0)

    output_dir = os.path.dirname(output_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir, mode=0755, exist_ok=True)

    logger.debug('Dumping data...')
    with codecs.open(output_path, 'w') as output_file:
        pickle.dump(data, output_file)
