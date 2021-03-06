import os

from reframe.core.pipeline import RegressionTest


class EmptyTest(RegressionTest):
    def __init__(self, **kwargs):
        super().__init__('emptycheck', os.path.dirname(__file__), **kwargs)


class InvalidTest:
    def __init__(self, **kwargs):
        pass


def _get_checks(**kwargs):
    return [EmptyTest(**kwargs), InvalidTest(**kwargs)]
