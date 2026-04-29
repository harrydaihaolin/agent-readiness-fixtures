import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from noisy_fixture.utils import do_thing  # noqa: E402


class TestSmoke(unittest.TestCase):
    def test_do_thing(self):
        self.assertEqual(do_thing(3), 6)


if __name__ == "__main__":
    unittest.main()
