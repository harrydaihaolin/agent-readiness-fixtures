import io
import os
import sys
import unittest
from contextlib import redirect_stdout

from thin_pkg.cli import main


class TestCli(unittest.TestCase):
    def test_default_greeting(self):
        os.environ.pop("THIN_PKG_GREETING", None)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main()
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "hi")

    def test_env_override(self):
        os.environ["THIN_PKG_GREETING"] = "howdy"
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main()
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "howdy")
        del os.environ["THIN_PKG_GREETING"]


if __name__ == "__main__":
    unittest.main()
