#python -m unittest discover -s tests

import unittest
import os
import sys
from unittest.mock import patch

from src.practice_1_CLI import navigate, ls, cd, main

class TestRepl(unittest.TestCase):
    def test_ls_no_args(self):
        result = navigate("ls", [])
        self.assertEqual(result, "ls []")

    def test_ls_with_args(self):
        result = navigate("ls", ["-p", "args"])
        self.assertEqual(result, "ls ['-p', 'args']")

    def test_cd_with_args(self):
        result = navigate("cd", ["c/"])
        self.assertEqual(result, "cd ['c/']")

    def test_cd_no_args(self):
        result = navigate("cd", [])
        self.assertEqual(result, "cd []")

    @patch('builtins.input', side_effect=['exit'])
    def test_exit(self, mock_input):
        test_args = ["practice_1_CLI.py", "--vfs", "./test_vfs"]

        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()

        self.assertEqual(cm.exception.code, 0)

    def test_unkown_command(self):
        result = navigate("unkown", ["/"])
        self.assertEqual(result, "unkown: команда не найдена")


if __name__ == '__main__':
    unittest.main()
