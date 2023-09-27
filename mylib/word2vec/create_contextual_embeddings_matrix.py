from typing import List, Any, Tuple
import numpy as np


def create_contextual_embeddings_matrix(context_dataset_id: List[Tuple[int, List[int]]], N: int) -> np.ndarray:
    matrix = np.zeros((N, N))
    for central_word, context in context_dataset_id:
        for context_word in context:
            matrix[central_word, context_word] += 1
    return matrix
