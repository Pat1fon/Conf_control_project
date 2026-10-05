#python -m unittest discover -s tests

import unittest
import os
import sys
from unittest.mock import patch

from src import practice_1_CLI
from src.practice_1_CLI import navigate, ls, cd, main

class TestRepl(unittest.TestCase):

    def setUp(self):
        #Вызывается перед каждым тестом. Заполняет тестовую VFS в памяти
        practice_1_CLI.vfs_tree = {
            "root": {
                "bin": {},
                "home": {
                    "user": {
                        "file.txt": "hello"
                    }
                }
            }
        }
        practice_1_CLI.current_path = ["root"]

    def test_ls_root(self):
        #Проверка ls в корневом каталоге
        result = practice_1_CLI.ls([])
        self.assertIn("bin", result)
        self.assertIn("home", result)

    def test_cd_valid_dir(self):
        #Проверка успешного перехода cd
        practice_1_CLI.cd(["home"])
        self.assertEqual(practice_1_CLI.current_path, ["root", "home"])

    def test_cd_invalid_dir(self):
        # Проверка cd в несуществующую папку
        result = practice_1_CLI.cd(["not_exist"])
        self.assertIn("cd: not_exist: Нет такого файла или директории", result)

    def test_cd_dot_dot(self):
        # Проверка cd ..
        practice_1_CLI.current_path = ["root", "home"]
        practice_1_CLI.cd([".."])
        self.assertEqual(practice_1_CLI.current_path, ["root"])

if __name__ == '__main__':
    unittest.main()
