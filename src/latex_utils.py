"""
Utility functions for LaTeX generation.
"""

import re


# LaTeX document templates
LATEX_PREAMBLE = r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{xcolor}
\usepackage{enumitem}

\begin{document}
"""

LATEX_POSTAMBLE = r"""
\end{document}
"""


def escape_latex(text):
    """
    Escapes LaTeX special characters in a given string.
    
    This function escapes all LaTeX special characters to prevent compilation errors:
    - &, %, $, #, _, {, }, ~, ^, and backslash are all properly escaped.
    - Unicode characters are normalized to ASCII-safe equivalents where possible
      (e.g., U+2212 MINUS SIGN → regular hyphen-minus)
    - Unicode arrows are converted to LaTeX arrow commands
    - Unicode superscripts are converted to LaTeX math mode superscripts
    
    Args:
        text: String to escape
        
    Returns:
        String with LaTeX special characters properly escaped and Unicode normalized
    """
    if not isinstance(text, str):
        return text
    
    # Normalize Unicode characters to ASCII-safe equivalents or LaTeX commands
    # U+2212 MINUS SIGN → U+002D HYPHEN-MINUS
    text = text.replace('\u2212', '-')  # MINUS SIGN → HYPHEN-MINUS
    
    # Unicode arrows → LaTeX arrow commands
    text = text.replace('\u2194', r'$\leftrightarrow$')  # LEFT RIGHT ARROW
    text = text.replace('\u2190', r'$\leftarrow$')  # LEFT ARROW
    text = text.replace('\u2192', r'$\rightarrow$')  # RIGHT ARROW
    text = text.replace('\u2191', r'$\uparrow$')  # UP ARROW
    text = text.replace('\u2193', r'$\downarrow$')  # DOWN ARROW
    
    # Greek letters → LaTeX Greek commands
    # Common lowercase Greek letters
    greek_letters_lower = {
        '\u03B1': r'$\alpha$',  # α
        '\u03B2': r'$\beta$',  # β
        '\u03B3': r'$\gamma$',  # γ
        '\u03B4': r'$\delta$',  # δ
        '\u03B5': r'$\epsilon$',  # ε
        '\u03B6': r'$\zeta$',  # ζ
        '\u03B7': r'$\eta$',  # η
        '\u03B8': r'$\theta$',  # θ
        '\u03B9': r'$\iota$',  # ι
        '\u03BA': r'$\kappa$',  # κ
        '\u03BB': r'$\lambda$',  # λ
        '\u03BC': r'$\mu$',  # μ
        '\u03BD': r'$\nu$',  # ν
        '\u03BE': r'$\xi$',  # ξ
        '\u03BF': r'$o$',  # ο (looks like Latin o)
        '\u03C0': r'$\pi$',  # π
        '\u03C1': r'$\rho$',  # ρ
        '\u03C2': r'$\varsigma$',  # ς (final sigma)
        '\u03C3': r'$\sigma$',  # σ (sigma)
        '\u03C4': r'$\tau$',  # τ
        '\u03C5': r'$\upsilon$',  # υ
        '\u03C6': r'$\phi$',  # φ
        '\u03C7': r'$\chi$',  # χ
        '\u03C8': r'$\psi$',  # ψ
        '\u03C9': r'$\omega$',  # ω
    }
    
    # Common uppercase Greek letters
    greek_letters_upper = {
        '\u0391': r'$\Alpha$',  # Α
        '\u0392': r'$\Beta$',  # Β
        '\u0393': r'$\Gamma$',  # Γ
        '\u0394': r'$\Delta$',  # Δ
        '\u0395': r'$\Epsilon$',  # Ε
        '\u0396': r'$\Zeta$',  # Ζ
        '\u0397': r'$\Eta$',  # Η
        '\u0398': r'$\Theta$',  # Θ
        '\u0399': r'$\Iota$',  # Ι
        '\u039A': r'$\Kappa$',  # Κ
        '\u039B': r'$\Lambda$',  # Λ
        '\u039C': r'$\Mu$',  # Μ
        '\u039D': r'$\Nu$',  # Ν
        '\u039E': r'$\Xi$',  # Ξ
        '\u039F': r'$O$',  # Ο (looks like Latin O)
        '\u03A0': r'$\Pi$',  # Π
        '\u03A1': r'$\Rho$',  # Ρ
        '\u03A3': r'$\Sigma$',  # Σ
        '\u03A4': r'$\Tau$',  # Τ
        '\u03A5': r'$\Upsilon$',  # Υ
        '\u03A6': r'$\Phi$',  # Φ
        '\u03A7': r'$\Chi$',  # Χ
        '\u03A8': r'$\Psi$',  # Ψ
        '\u03A9': r'$\Omega$',  # Ω
    }
    
    # Replace Greek letters with LaTeX commands
    all_greek = {**greek_letters_lower, **greek_letters_upper}
    for greek_char, latex_cmd in all_greek.items():
        text = text.replace(greek_char, latex_cmd)
    
    # Mathematical symbols → LaTeX commands
    math_symbols = {
        '\u2265': r'$\geq$',  # ≥ (greater than or equal)
        '\u2264': r'$\leq$',  # ≤ (less than or equal)
        '\u2211': r'$\sum$',  # ∑ (summation)
        '\u222B': r'$\int$',  # ∫ (integral)
        '\u2208': r'$\in$',  # ∈ (element of)
        '\u2209': r'$\notin$',  # ∉ (not element of)
        '\u2200': r'$\forall$',  # ∀ (for all)
        '\u2203': r'$\exists$',  # ∃ (exists)
        '\u221E': r'$\infty$',  # ∞ (infinity)
        '\u00B1': r'$\pm$',  # ± (plus-minus)
        '\u2212': r'$-$',  # − (already handled as minus, but ensure it's handled)
    }
    
    # Replace mathematical symbols
    for symbol_char, latex_cmd in math_symbols.items():
        text = text.replace(symbol_char, latex_cmd)
    
    # Unicode superscripts → LaTeX math mode superscripts
    # Common superscripts
    superscript_map = {
        '\u00B9': '1',  # ¹
        '\u00B2': '2',  # ²
        '\u00B3': '3',  # ³
        '\u2074': '4',  # ⁴
        '\u2075': '5',  # ⁵
        '\u2076': '6',  # ⁶
        '\u2077': '7',  # ⁷
        '\u2078': '8',  # ⁸
        '\u2079': '9',  # ⁹
        '\u2070': '0',  # ⁰
    }
    
    # Mathematical superscripts (U+1D40-U+1D7F) → map to corresponding ASCII letters
    # These are modifier letters that represent superscript versions of letters
    mathematical_superscript_map = {
        # Map mathematical superscripts to their base letters
        # U+1D40-1D4F: Mathematical Script Capital letters
        '\u1D40': 'T', '\u1D41': 'U', '\u1D42': 'V', '\u1D43': 'W',
        '\u1D44': 'X', '\u1D45': 'Y', '\u1D46': 'Z', '\u1D47': 'a',
        '\u1D48': 'b', '\u1D49': 'c', '\u1D4A': 'd', '\u1D4B': 'e',
        '\u1D4C': 'f', '\u1D4D': 'g', '\u1D4E': 'h', '\u1D4F': 'i',
        # Add more mappings for the full range U+1D40-1D7F
        # For now, we'll handle the common ones and use a fallback for others
    }
    
    # Unicode subscripts (U+2080-U+209F) → map to base characters
    subscript_map = {
        '\u2080': '0', '\u2081': '1', '\u2082': '2', '\u2083': '3',
        '\u2084': '4', '\u2085': '5', '\u2086': '6', '\u2087': '7',
        '\u2088': '8', '\u2089': '9',
        '\u2090': 'a', '\u2091': 'e', '\u2092': 'o', '\u2093': 'x',
        '\u2094': 'e', '\u2095': 'h', '\u2096': 'k', '\u2097': 'l',  # U+2094 is schwa (ə) → use 'e'
        '\u2098': 'm', '\u2099': 'n', '\u209A': 'p', '\u209B': 's',
        '\u209C': 't',
    }
    
    # Replace superscripts, mathematical superscripts, and subscripts with LaTeX math mode
    # We'll process these character by character to handle properly
    result_chars = []
    i = 0
    while i < len(text):
        char = text[i]
        replacement = None
        
        if char in superscript_map:
            replacement = superscript_map[char]
        elif char in mathematical_superscript_map:
            # Mathematical superscript - convert to base letter in superscript
            replacement = mathematical_superscript_map[char]
        elif char in subscript_map:
            # Subscript - convert to base character in subscript
            replacement = subscript_map[char]
        elif 0x1D40 <= ord(char) <= 0x1D7F:
            # Mathematical superscript range - convert to ASCII equivalent
            # Try to map to corresponding letter (simple approximation)
            # For mathematical script capitals, map to regular capitals
            if 0x1D40 <= ord(char) <= 0x1D7F:
                # Try to decode: U+1D40 is 'T' superscript, etc.
                # Map to regular ASCII letter
                base_code = ord(char) - 0x1D40
                if base_code < 26:
                    replacement = chr(ord('A') + base_code)
                elif base_code < 52:
                    replacement = chr(ord('a') + base_code - 26)
                else:
                    # Fallback: use regular T (most common)
                    replacement = 'T'
        elif 0x2090 <= ord(char) <= 0x209F:
            # Subscript range - convert to base character
            base_code = ord(char) - 0x2090
            if base_code < 10:
                replacement = str(base_code)
            else:
                # Map to common subscript letters
                subscript_chars = ['a', 'e', 'o', 'x', 'ə', 'h', 'k', 'l', 'm', 'n', 'p', 's', 't']
                if base_code - 10 < len(subscript_chars):
                    replacement = subscript_chars[base_code - 10]
                else:
                    replacement = 'x'  # Fallback
        
        if replacement:
            # Found a superscript/subscript - convert to LaTeX math mode
            # Check if previous char was part of a word (for proper formatting)
            if result_chars and result_chars[-1] not in [' ', '$', '{', '}']:
                # Insert math mode with superscript/subscript
                result_chars.append('$^{')
                result_chars.append(replacement)
                result_chars.append('}$')
            else:
                # Standalone superscript/subscript
                result_chars.append('$^{')
                result_chars.append(replacement)
                result_chars.append('}$')
        else:
            result_chars.append(char)
        i += 1
    
    text = ''.join(result_chars)
    
    # Use temporary placeholders for characters that need special handling
    # Use unique markers that won't conflict with text content
    placeholder_backslash = '\x01\x02\x03BACK\x03\x04\x05'
    placeholder_math_start = '\x06\x07\x08MATHSTART\x09\x0a\x0b'
    placeholder_math_end = '\x0c\x0d\x0eMATHEND\x0f\x10\x11'
    
    # FIRST: Protect math mode expressions by replacing them with placeholders
    # This must happen BEFORE backslash escaping to preserve LaTeX commands
    math_replacements = []
    import re
    
    def protect_math(match):
        math_expr = match.group(0)
        math_replacements.append(math_expr)
        return placeholder_math_start + str(len(math_replacements) - 1) + placeholder_math_end
    
    # Match Greek letter math mode patterns: $\sigma$, $\mu$, etc.
    # Pattern: $ followed by backslash, then letters, then $
    greek_pattern = r'\$\\([a-zA-Z]+)\$'  # Matches $\alpha$, $\sigma$, $\Gamma$, etc.
    text = re.sub(greek_pattern, protect_math, text)
    
    # Match $^{digit}$ and $^{letter}$ patterns (for superscripts/subscripts)
    math_pattern = r'\$\^\{[0-9A-Za-z]\}\$'
    text = re.sub(math_pattern, protect_math, text)
    
    # Also handle arrow patterns $\\leftrightarrow$ etc (already have double backslash)
    arrow_pattern = r'\$\\leftrightarrow\$|\$\\leftarrow\$|\$\\rightarrow\$|\$\\uparrow\$|\$\\downarrow\$'
    text = re.sub(arrow_pattern, protect_math, text)
    
    # Also handle simple math expressions like $o$, $O$ (Greek letters that look like Latin)
    simple_math_pattern = r'\$[a-zA-Z]\$'  # Matches $o$, $O$, etc.
    text = re.sub(simple_math_pattern, protect_math, text)
    
    # NOW handle backslashes in non-protected text (after math mode is protected)
    text = text.replace('\\', placeholder_backslash)
    
    # Escape all LaTeX special characters (must escape backslash LAST)
    # Order matters: escape special chars first, then restore backslashes
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('$', r'\$')  # Escape standalone $ signs (but protected ones are already replaced)
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    text = text.replace('{', r'\{')
    text = text.replace('}', r'\}')
    text = text.replace('~', r'\textasciitilde{}')
    text = text.replace('^', r'\textasciicircum{}')
    
    # Restore math mode expressions (these should not be escaped, they already have proper LaTeX commands)
    for i, math_expr in enumerate(math_replacements):
        text = text.replace(placeholder_math_start + str(i) + placeholder_math_end, math_expr)
    
    # Restore original backslashes (these are user-provided backslashes, not LaTeX commands)
    # Replace placeholder with escaped backslash representation
    text = text.replace(placeholder_backslash, r'\textbackslash{}')
    
    return text


def generate_question_latex(question):
    """
    Generates the LaTeX for a single question.
    
    Args:
        question: Dictionary containing question data
        
    Returns:
        String containing LaTeX-formatted question
    """
    lines = []

    # Metadata
    lines.append("\\begin{tabular}{|l|l|}")
    lines.append("\\hline")
    lines.append(f"**Question ID:** & {escape_latex(question.get('questionId', 'N/A'))} \\\\ \\hline")
    lines.append(f"**Topic:** & {escape_latex(question.get('topic', 'N/A'))} \\\\ \\hline")
    lines.append(f"**Difficulty:** & {escape_latex(question.get('metadata', {}).get('difficulty', 'N/A'))} \\\\ \\hline")
    lines.append(f"**Blooms:** & {escape_latex(question.get('metadata', {}).get('blooms', 'N/A'))} \\\\ \\hline")
    lines.append("\\end{tabular}")
    lines.append("")

    # Question text
    lines.append(f"\\subsection*{{{escape_latex(question.get('questionText', ''))}}}")

    # Options
    if question.get("questionType") == "Multiple Choice":
        lines.append("\\begin{enumerate}")
        for option in question.get("options", []):
            text = escape_latex(option.get("text", ""))
            if option.get("isCorrect"):
                lines.append(f"\\item \\textcolor{{green}}{{{text}}}")
            else:
                lines.append(f"\\item {text}")
        lines.append("\\end{enumerate}")

    return "\n".join(lines)


def generate_latex_document(questions, question_separator="\\vspace{1cm}\n\n"):
    """
    Generates a complete LaTeX document from a list of questions.
    
    Args:
        questions: List of question dictionaries
        question_separator: String to insert between questions (default: vertical space)
        
    Returns:
        String containing complete LaTeX document
    """
    latex_body = ""
    for question in questions:
        latex_body += generate_question_latex(question)
        latex_body += question_separator
    
    return LATEX_PREAMBLE + latex_body + LATEX_POSTAMBLE


def write_latex_file(filepath, questions, question_separator="\\vspace{1cm}\n\n"):
    """
    Writes a LaTeX document to a file.
    
    Args:
        filepath: Path to output LaTeX file
        questions: List of question dictionaries
        question_separator: String to insert between questions (default: vertical space)
    """
    latex_content = generate_latex_document(questions, question_separator)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(latex_content)
