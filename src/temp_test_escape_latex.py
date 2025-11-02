
import unittest
from temp_escape_latex import escape_latex

class TestEscapeLatex(unittest.TestCase):

    def test_single_special_characters(self):
        self.assertEqual(escape_latex("a & b"), r"a \& b")
        self.assertEqual(escape_latex("a % b"), r"a \% b")
        self.assertEqual(escape_latex("a $ b"), r"a \$ b")
        self.assertEqual(escape_latex("a # b"), r"a \# b")
        self.assertEqual(escape_latex("a _ b"), r"a \_ b")
        self.assertEqual(escape_latex("a { b"), r"a \{ b")
        self.assertEqual(escape_latex("a } b"), r"a \} b")
        self.assertEqual(escape_latex("a ~ b"), r"a \textasciitilde{} b")
        self.assertEqual(escape_latex("a ^ b"), r"a \textasciicircum{} b")
        self.assertEqual(escape_latex("a \ b"), r"a \\textbackslash{} b")

    def test_multiple_special_characters(self):
        self.assertEqual(escape_latex("a & % $ # _ { } ~ ^ \ b"), r"a \& \% \$ \# \_ \{ \} \textasciitilde{} \textasciicircum{} \\textbackslash{} b")

    def test_synthetic_inputs(self):
        self.assertEqual(escape_latex("variable1 $ variable2"), r"variable1 \$ variable2")
        self.assertEqual(escape_latex("first $ second"), r"first \$ second")

    def test_no_special_characters(self):
        self.assertEqual(escape_latex("a and b"), "a and b")

    def test_empty_string(self):
        self.assertEqual(escape_latex(""), "")

if __name__ == '__main__':
    unittest.main()
