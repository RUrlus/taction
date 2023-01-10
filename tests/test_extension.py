import numpy as np
import taction


def test_add():
    assert taction.ext.add(1, 1) == 2


def test_arange():
    ubs = np.random.randint(2, 1000, size=100)
    for ub in ubs:
        step = np.random.randint(1, ub)
        np.testing.assert_equal(
            taction.ext.arange(0, ub, step=step), np.arange(ub, step=step)
        )
