from syllabus_comparison.model import load_model
from syllabus_comparison.extract_topics import extract_topics
from syllabus_comparison.similarity import calculate_similarity, find_best_match
from syllabus_comparison.report import generate_comparison_stats

def compare_syllabi(old_syllabus, new_syllabus, similarity_threshold=0.6):
    """Compares old and new syllabi for added, removed, and matched topics."""
    
    # Load model once and reuse
    model = load_model()
    
    # Extract topics
    old_topics = extract_topics(old_syllabus)
    new_topics = extract_topics(new_syllabus)

    # Generate embeddings
    old_embeddings = model.encode([t[0] for t in old_topics], convert_to_tensor=True)
    new_embeddings = model.encode([t[0] for t in new_topics], convert_to_tensor=True)

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
