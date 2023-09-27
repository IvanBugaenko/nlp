from typing import List


def drop_stopwords(words: List[str], stopwords: List[str], **kwargs) -> List[str]:
    return [word for word in words if word not in stopwords]
