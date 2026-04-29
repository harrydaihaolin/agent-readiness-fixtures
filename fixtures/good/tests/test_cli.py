import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from good_fixture.cli import main  # noqa: E402


class TestCli(unittest.TestCase):
    def test_default_greeting(self):
        os.environ.pop("GREETING", None)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main()
        self.assertEqual(rc, 0)
        self.assertIn("Hello", buf.getvalue())

    def test_env_override(self):
        os.environ["GREETING"] = "Hi"
        try:
            buf = io.StringIO()
            with redirect_stdout(buf):
                main()
            self.assertIn("Hi", buf.getvalue())
        finally:
            os.environ.pop("GREETING", None)


if __name__ == "__main__":
    unittest.main()
