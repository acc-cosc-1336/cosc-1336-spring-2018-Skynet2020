import unittest

from tests.assignments import test_homework7

suite = unittest.TestLoader().loadTestsFromModule(test_homework7)
unittest.TextTestRunner(verbosity=2).run(suite)
