from typing import List
from pymorphy3 import MorphAnalyzer


morph = MorphAnalyzer()


def lemmatization(words: List[str], **kwargs) -> List[str]:
    return list(map(lambda word: morph.normal_forms(word)[0], words))
