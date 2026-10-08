import io, os, tempfile, unittest
from contextlib import redirect_stdout
from command import MyCommand

class CliTests(unittest.TestCase):
    def setUp(self):
        self.old = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory() #starting directory to allow for testing directory changes
        os.chdir(self.tmp.name)
        self.shell = MyCommand()

    def tearDown(self):
        os.chdir(self.old)
        self.tmp.cleanup()

    def run_cmd(self, line):
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.shell.onecmd(line)
        return buf.getvalue()

    def test_rm_removes_a_file(self):
        open("a.txt" ,"w").close()
        self.run_cmd("rm a.txt")
        self.assertFalse(os.path.exists("a.txt"))

    def test_cd_changes_directory(self):
        os.mkdir("test_dir")
        self.run_cmd("cd test_dir")
        self.assertEqual(os.getcwd(), os.path.join(self.tmp.name, "test_dir"))

    def test_cd_invalid_directory(self):
        self.run_cmd("cd invalid_dir")
        self.assertEqual(os.getcwd(), self.tmp.name)  # Should remain in the original directory

    def test_ls_lists_files(self):
        open("file1.txt", "w").close()
        open("file2.txt", "w").close()
        output = self.run_cmd("ls")
        self.assertIn("file1.txt", output)
        self.assertIn("file2.txt", output)

    def test_mv_moves_file(self):
        open("file1.text", "w").close()
        os.mkdir("target_dir")
        self.run_cmd("mv file1.text target_dir")
        self.assertTrue(os.path.exists("target_dir/file1.text"))
        