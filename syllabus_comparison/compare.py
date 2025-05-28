from syllabus_comparison.model import load_models
from syllabus_comparison.extract_topics import extract_topics
from syllabus_comparison.similarity import calculate_similarity, find_best_match
from syllabus_comparison.report import generate_comparison_stats
from sklearn.preprocessing import normalize
import numpy as np

def combined_embeddings(texts, model1, model2):
    emb1 = model1.encode(texts, convert_to_numpy=True)
    emb2 = model2.encode(texts, convert_to_numpy=True)
    combined = np.concatenate([emb1, emb2], axis=1)
    return normalize(combined)


def compare_syllabi(old_syllabus, new_syllabus, similarity_threshold=0.6):
    """Compares old and new syllabi for added, removed, and matched topics."""
    
    
    old_topics = extract_topics(old_syllabus)
    new_topics = extract_topics(new_syllabus)

   
    model1, model2 = load_models()
    texts_old = [t[0] for t in old_topics]
    texts_new = [t[0] for t in new_topics]

    old_embeddings = combined_embeddings(texts_old, model1, model2)
    new_embeddings = combined_embeddings(texts_new, model1, model2)


    # Initialize results
    added, removed, matches, elaborations, shifted = [], [], [], [], []

    # Compare new syllabus topics to old syllabus topics
    for i, (new_topic, new_unit, new_label) in enumerate(new_topics):
        similarities = calculate_similarity(new_embeddings[i], old_embeddings).squeeze()
        max_similarity, best_match_index = find_best_match(similarities, similarity_threshold)
        
        if best_match_index is not None:
            old_topic, old_unit, old_label = old_topics[best_match_index]
            if new_unit != old_unit:
                shifted.append({"topic": new_topic, "from": old_label, "to": new_label})
            else:
                matches.append({"new": new_topic, "old": old_topic, "similarity": max_similarity})
        elif max_similarity >= similarity_threshold - 0.1:
            elaborations.append({"new": new_topic, "old": old_topic, "similarity": max_similarity})
        else:
            added.append(new_topic)

    # Compare old syllabus topics to new syllabus topics
    for i, (old_topic, old_unit, old_label) in enumerate(old_topics):
        similarities = calculate_similarity(old_embeddings[i], new_embeddings).squeeze()
        max_similarity = similarities.max().item()
        if max_similarity < similarity_threshold - 0.1:
            removed.append(old_topic)

    comparison_result = {"added": added,
        "removed": removed,
        "semantic_matches": matches,
        "elaborations": elaborations,
        "shifted_topics": shifted}

    stats = generate_comparison_stats(comparison_result)      
   

    return {
        "added": added,
        "removed": removed,
        "semantic_matches": matches,
        "elaborations": elaborations,
        "shifted_topics": shifted,
        "stats":stats
    }
