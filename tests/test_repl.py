#python -m unittest discover -s tests

import unittest
import os
import sys
from datetime import datetime
from unittest.mock import patch

from src import practice_1_CLI
from src.practice_1_CLI import navigate, ls, cd, main

class TestRepl(unittest.TestCase):

    def setUp(self):
        #Вызывается перед каждым тестом. Заполняет тестовую VFS в памяти
        practice_1_CLI.vfs_tree = {

                "bin": {},
                "home": {
                    "user": {
                        "file.txt": "hello"
                    }
                }
            }

        practice_1_CLI.current_path = []

    def test_ls_root(self):
        #Проверка ls в корневом каталоге
        result = practice_1_CLI.ls([])
        self.assertIn("bin", result)
        self.assertIn("home", result)

    def test_cd_valid_dir(self):
        #Проверка успешного перехода cd
        practice_1_CLI.cd(["home"])
        self.assertEqual(practice_1_CLI.current_path, ["home"])

    def test_cd_invalid_dir(self):
        # Проверка cd в несуществующую папку
        result = practice_1_CLI.cd(["not_exist"])
        self.assertIn("cd: not_exist: Нет такого файла или директории", result)

    def test_cd_dot_dot(self):
        # Проверка cd ..
        practice_1_CLI.current_path = ["home"]
        practice_1_CLI.cd([".."])
        self.assertEqual(practice_1_CLI.current_path, [])

    def test_date_command(self):
        # Проверка команды date
        result = practice_1_CLI.date_cmd([])
        current_year = str(datetime.now().year)
        self.assertIn(current_year, result)
        self.assertIn("MSK", result)

    def test_tree_command(self):
        # Проверка команды tree
        result = practice_1_CLI.tree_cmd([])
        self.assertIn("|--bin", result)
        self.assertIn("^--home", result)
        self.assertIn("file.txt", result)

    def test_du_command(self):
        # Проверка работы du
        result = practice_1_CLI.du_cmd([])
        self.assertIn("bin: 0", result)
        self.assertIn("home: 5", result)

    @patch('builtins.input', side_effect=['exit'])
    def test_exit_command(self, mock_input):
        # Проверка команды exit
        test_args = ["practice_1_CLI.py", "--vfs", "vfs_config.json"]

        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()

        self.assertEqual(cm.exception.code, 0)
if __name__ == '__main__':
    unittest.main()
