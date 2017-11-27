# -*- coding: utf-8 -*-

import logging
import os


__all__ = (
    'LOGGER_NAME',
    'get_default_logger',
)


LOGGER_NAME = 'wf-ds-tools'


streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)s.%(funcName)s: %(message)s')
streamHandler.setFormatter(formatter)

fileHandler = logging.FileHandler(os.path.expanduser('~/tmp/{}.log'.format(LOGGER_NAME)))
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.INFO)
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)
logger.propagate = False


def get_default_logger():
    return logger
