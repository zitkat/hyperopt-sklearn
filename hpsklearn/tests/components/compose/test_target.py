import unittest

from hpsklearn import transformed_target_regressor
from hpsklearn.tests.utils import \
    StandardRegressorTest, \
    generate_test_attributes


class TestTransformedTargetRegression(StandardRegressorTest):
    """
    Class for _target regression testing
    """


generate_test_attributes(
    TestClass=TestTransformedTargetRegression,
    fn_list=[transformed_target_regressor],
    is_classif=False,
    non_negative_input=True,
    non_negative_output=True,
)


if __name__ == '__main__':
    unittest.main()
