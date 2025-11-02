
import re

def escape_latex(text):
    """
    Escapes LaTeX special characters in a given string.
    """
    if not isinstance(text, str):
        return text

    replacements = dict([
        ('&', r'\\&'),
        ('%', r'\\%'),
        ('$', r'\\$'),
        ('#', r'\\#'),
        ('_', r'\\_'),
        ('{', r'\\{'),
        ('}', r'\\}'),
        ('~', r'\\textasciitilde{}'),
        ('^', r'\\textasciicircum{}'),
        ('\\', r'\\textbackslash{}')
    ])

    regex_pattern = re.compile(
        '|'.join(re.escape(key) for key in sorted(replacements.keys(), key=len, reverse=True))
    )

    return regex_pattern.sub(lambda match: replacements[match.group(0)], text)
