import io, os, tempfile, unittest
from contextlib import redirect_stdout
from command import MyCommand

class CliTests(unittest.TestCase):
    def setUp(self):
        self.old = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
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