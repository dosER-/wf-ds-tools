# -*- coding: utf-8 -*-

import sklearn.tree as tree

from dstools.utils.args import (Arg, filter_kwargs, )
from dstools.utils.log import (get_default_logger, )


__all__ = (
    'DEFAULT_KWARGS',
    'ARGS',

    'fit',
)

ARGS = [
    Arg(
        flags=['-c', '--criterion'],
        dest='criterion', type=str, choices=('gini', 'entropy', ),
        help='The function to measure the quality of a split (default: {default})'
    ),
    Arg(
        flags=['-s', '--splitter'],
        dest='splitter', type=str, choices=('best', 'random', ),
        help='The strategy used to choose the split at each node (default: {default})'
    ),
    Arg(
        flags=['-md', '--max-depth'],
        dest='max_depth', type=int, choices=None,
        help='The maximum depth of the tree (default: {default})'
    ),
    Arg(
        flags=['-mss', '--min-samples-split'],
        dest='min_samples_split', type= int, choices = None,
        help = 'The minimum number of samples required to split an internal node (default: {default})'
    ),
    Arg(
        flags=['-msl', '--min-samples-leaf'],
        dest='min_samples_leaf', type=int, choices=None,
        help='The minimum number of samples required to be at a leaf node (default: {default})'
    ),
]
ARGS_MAP = {arg.dest: arg for arg in ARGS}
DEFAULT_KWARGS = {
    'criterion': 'gini',
    'splitter': 'best',
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
    'min_weight_fraction_leaf': 0.,
    'max_features': None,
    'random_state': None,
    'max_leaf_nodes': None,
    'min_impurity_decrease': 0.,
    'min_impurity_split': None,
    'class_weight': None,
    'presort': False,
}


logger = get_default_logger()

@filter_kwargs(ctx='dtc.fit', args_map=ARGS_MAP)
def fit(X, y, logger=logger, **kwargs):
    """Build a decision tree classifier from the training set (X, y).
    Parameters
    ----------
    X : array-like or sparse matrix, shape = [n_samples, n_features]
        The training input samples. Internally, it will be converted to
        ``dtype=np.float32`` and if a sparse matrix is provided
        to a sparse ``csc_matrix``.
    y : array-like, shape = [n_samples] or [n_samples, n_outputs]
        The target values (class labels) as integers or strings.
        sample_weight : array-like, shape = [n_samples] or None
        Sample weights. If None, then samples are equally weighted. Splits
        that would create child nodes with net zero or negative weight are
        ignored while searching for a split in each node. Splits are also
        ignored if they would result in any single class carrying a
        negative weight in either child node.
    logger : logging.Logger
        Custom or default logger
    **kwargs : dict
        DTC params
    Returns
    -------
    dtc : sklearn.tree.DecisionTreeClassifier
        Returns dtc`.
    """

    # DTC init params
    dtc_kwargs = dict(DEFAULT_KWARGS)
    # Update default params by input
    dtc_kwargs.update(kwargs)
    # Init classifier
    dtc = tree.DecisionTreeClassifier(**dtc_kwargs)
    # Fit classifier
    logger.info('Fitting DTC...')
    dtc.fit(X, y)

    return dtc
