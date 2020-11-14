# -*- coding: utf-8 -*-
"""
The root of the greenlet package.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__all__ = [
    '__version__',
    '_C_API',

    'GreenletExit',
    'error',

    'getcurrent',
    'greenlet',

    'gettrace',
    'settrace',
]

# pylint:disable=no-name-in-module

###
# Metadata
###
from ._greenlet import __version__
# TODO: Move the definition of __version__ here, instead of the
# C code. zest.releaser will find it here, but not in C.
from ._greenlet import _C_API # pylint:disable=no-name-in-module

###
# Exceptions
###
from ._greenlet import GreenletExit
from ._greenlet import error

###
# greenlets
###
from ._greenlet import getcurrent
from ._greenlet import greenlet

###
# tracing
###
try:
    from ._greenlet import gettrace
    from ._greenlet import settrace
except ImportError:
    # Tracing wasn't supported.
    # TODO: Remove the option to disable it.
    pass

###
# Constants
# These constants aren't documented and aren't recommended
###
from ._greenlet import GREENLET_USE_CONTEXT_VARS # pylint:disable=unused-import
from ._greenlet import GREENLET_USE_GC # pylint:disable=unused-import
from ._greenlet import GREENLET_USE_TRACING # pylint:disable=unused-import