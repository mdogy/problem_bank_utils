
def escape_latex(text):
    """
    Escapes LaTeX special characters in a given string.
    """
    assert isinstance(text, str), "Input must be a string."
    text = text.replace('\\', r'\\\\\\textbackslash{}')
    text = text.replace('&', r'\\&')
    text = text.replace('%', r'\\%')
    text = text.replace('$', r'\\$')
    text = text.replace('#', r'\\#')
    text = text.replace('_', r'\\_')
    text = text.replace('{', r'\\{')
    text = text.replace('}', r'\\}')
    text = text.replace('~', r'\\textasciitilde{}')
    text = text.replace('^', r'\\textasciicircum{}')
    return text
