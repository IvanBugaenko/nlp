from typing import List
from nltk.corpus import stopwords


stopwords_all_language = {
    "ru": stopwords.words('russian')
}


def drop_stopwords(words: List[str], language: str, **kwargs) -> List[str]:
    return [word for word in words if word not in stopwords_all_language[language]]
