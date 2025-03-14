from sentence_transformers import util

def calculate_similarity(new_embeddings, old_embeddings):
    """Computes cosine similarity matrix between old and new syllabus topics."""
    return util.cos_sim(new_embeddings, old_embeddings)

def find_best_match(similarities, threshold):
    """Finds the best match index and similarity score."""
    max_similarity, max_index = similarities.max().item(), similarities.argmax().item()
    return max_similarity, max_index if max_similarity >= threshold else None
