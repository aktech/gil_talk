import unittest

from extension_module import count
from c_extension_gil import run_count_in_single_thread
from c_extension_gil import run_count_in_multiple_threads


class TestCExtensionCount(unittest.TestCase):

    def test_count_function(self):
        self.assertEqual(count(int(10e5)), 1)

    def test_run_count_in_single_thread(self):
        time_taken = run_count_in_single_thread()
        self.assertGreater(time_taken, 0)

    def test_run_count_in_multiple_threads(self):
        time_taken = run_count_in_multiple_threads()
        self.assertGreater(time_taken, 0)

    def test_count_multiple_thread_faster_than_single_thread(self):
        single_thread_time_taken = run_count_in_single_thread()
        multiple_thread_time_taken = run_count_in_multiple_threads()
        self.assertGreater(single_thread_time_taken, multiple_thread_time_taken)
