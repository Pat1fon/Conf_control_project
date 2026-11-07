import unittest
import sys
from unittest.mock import patch
from datetime import datetime
import src.practice_1_CLI as cli


class TestRepl(unittest.TestCase):

    def init_test_vfs(self):
        """Инициализирует дерево VFS в памяти перед тестами (PEP8-style)."""
        cli.vfs_tree = {
            "bin": {},
            "home": {
                "user": {
                    "file.txt": "hello"
                }
            }
        }
        cli.current_path = []

    def test_ls_root(self):
        """Проверяет команду ls в корневом каталоге VFS."""
        self.init_test_vfs()
        result = cli.ls([])
        self.assertIn("bin", result)
        self.assertIn("home", result)

    def test_cd_valid_dir(self):
        """Проверяет успешное изменение директории эмулятора."""
        self.init_test_vfs()
        cli.cd("home")
        self.assertEqual(cli.current_path, ["home"])

    def test_cd_invalid_dir(self):
        """Проверяет обработку ошибок при переходе в неверный путь."""
        self.init_test_vfs()
        result = cli.cd("not_exist")
        self.assertIn("cd: not_exist: Нет такого файла", result)

    def test_cd_dot_dot(self):
        """Проверяет корректность относительного перехода на уровень вверх."""
        self.init_test_vfs()
        cli.current_path = ["home", "user"]
        cli.cd("..")
        self.assertEqual(cli.current_path, ["home"])

    def test_date_command(self):
        """Проверяет формат вывода текущей даты и часового пояса."""
        self.init_test_vfs()
        result = cli.date_cmd([])
        current_year = str(datetime.now().year)
        self.assertIn(current_year, result)
        self.assertIn("MSK", result)

    def test_tree_command(self):
        """Проверяет генерацию псевдографического дерева структуры каталогов."""
        self.init_test_vfs()
        result = cli.tree_cmd([])
        self.assertIn("bin", result)
        self.assertIn("home", result)
        self.assertIn("file.txt", result)

    def test_du_command(self):
        """Проверяет точность вычисления размера файлов в байтах."""
        self.init_test_vfs()
        result = cli.du_cmd([])
        self.assertIn("0\tbin", result)
        self.assertIn("5\thome", result)

    @patch('builtins.input', side_effect=['exit'])
    def test_exit_command(self, mock_input):
        """Проверяет системный код завершения программы при вызове exit."""
        self.init_test_vfs()
        test_args = ["practice_1_CLI.py", "--vfs", "vfs_config.json"]
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                cli.main()
        self.assertEqual(cm.exception.code, 0)


if __name__ == '__main__':
    unittest.main()

