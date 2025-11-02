import unittest
from temp_escape_single_char import escape_latex

class TestEscapeLatex(unittest.TestCase):

    def test_escape_ampersand(self):
        self.assertEqual(escape_latex("a & b"), r"a \& b")

    def test_escape_percent(self):
        self.assertEqual(escape_latex("a % b"), r"a \% b")

    def test_escape_dollar(self):
        self.assertEqual(escape_latex("a $ b"), r"a \$ b")

    def test_escape_hash(self):
        self.assertEqual(escape_latex("a # b"), r"a \# b")

    def test_escape_underscore(self):
        self.assertEqual(escape_latex("a _ b"), r"a \_ b")

    def test_escape_lbrace(self):
        self.assertEqual(escape_latex("a { b"), r"a \{ b")

    def test_escape_rbrace(self):
        self.assertEqual(escape_latex("a } b"), r"a \} b")

    def test_escape_tilde(self):
        self.assertEqual(escape_latex("a ~ b"), r"a \textasciitilde{} b")

    def test_escape_circumflex(self):
        self.assertEqual(escape_latex("a ^ b"), r"a \textasciicircum{} b")

    def test_escape_backslash(self):
        self.assertEqual(escape_latex("a \ b"), r"a \\textbackslash{} b")

if __name__ == '__main__':
    unittest.main()