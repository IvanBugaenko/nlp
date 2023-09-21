from typing import Dict
import re


def apply_regular_expressions(s: str, sub_expressions: Dict[str, str], **kwargs) -> str:
    text = s
    for pattern, repl in sub_expressions.items():
        text = re.sub(pattern, repl, text)
    return text
