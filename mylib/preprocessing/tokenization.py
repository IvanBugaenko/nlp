from typing import List
from nltk.tokenize import word_tokenize


tokenization_types = {
    "word": word_tokenize
}


def tokenization(s: str, tokenization_type: str, **kwargs) -> List[str]:
    return tokenization_types[tokenization_type](s)
