def generate_comparison_stats(comparison_result):
    """
    Generates statistical summary of syllabus changes.
    
    :param comparison_result: Dictionary output from the compare function.
    :return: Dictionary containing statistics.
    """
    added_count = len(comparison_result.get("added", []))
    removed_count = len(comparison_result.get("removed", []))
    semantic_matches_count = len(comparison_result.get("semantic_matches", []))
    elaborations_count = len(comparison_result.get("elaborations", []))
    shifted_topics_count = len(comparison_result.get("shifted_topics", []))

    total_changes = added_count + removed_count + semantic_matches_count + elaborations_count + shifted_topics_count

    retained_percentage = (
        (semantic_matches_count / (semantic_matches_count + removed_count) * 100)
        if (semantic_matches_count + removed_count) > 0 else 0
    )
    new_content_percentage = (
        (added_count / (added_count + semantic_matches_count) * 100)
        if (added_count + semantic_matches_count) > 0 else 0
    )
    topic_shift_impact = (
        (shifted_topics_count / total_changes * 100)
        if total_changes > 0 else 0
    )

    stats = {
        "total_added": added_count,
        "total_removed": removed_count,
        "total_semantic_matches": semantic_matches_count,
        "total_elaborations": elaborations_count,
        "total_shifted_topics": shifted_topics_count,
        "retained_percentage": f"{retained_percentage:.2f}%",
        "new_content_percentage": f"{new_content_percentage:.2f}%",
        "topic_shift_impact": f"{topic_shift_impact:.2f}%"
    }

    return stats 
