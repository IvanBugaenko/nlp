from pathlib import Path
import os
import sys

sys.path.append(str(Path(os.getcwd())))


from typing import List, Any
from mylib.preprocessing.apply_regular_expressions import apply_regular_expressions
from mylib.preprocessing.tokenization import tokenization
from mylib.preprocessing.lemmatization import lemmatization
from mylib.preprocessing.drop_stopwords import drop_stopwords


commands = {
    "apply_regular_expressions": apply_regular_expressions,
    "tokenize": tokenization,
    "lemmatization": lemmatization,
    "drop_stopwords": drop_stopwords
}


def preprocessing(text_document: str | List[str], pipeline: List[str], **kwargs) -> Any:
    temp = text_document
    for command in pipeline:
        temp = commands[command](temp, **kwargs)
    return temp
