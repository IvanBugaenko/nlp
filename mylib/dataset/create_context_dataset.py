from typing import List, Any, Tuple


def create_context_dataset(text_corpus: List[Any], window: int) -> List[Tuple[Any, List[Any]]]:
    return [(text_corpus[i], [text_corpus[i + j] for j in set(range(-window, window + 1)) if j != 0]) for i in range(window, len(text_corpus) - window)]
