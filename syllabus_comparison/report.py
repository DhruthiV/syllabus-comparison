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
        "Total Added": added_count,
        "Total Removed": removed_count,
        "Total Semantic Matches": semantic_matches_count,
        "Total Elaborations": elaborations_count,
        "Total Shifted Topics": shifted_topics_count,
        "Retained Percentage": f"{retained_percentage:.2f}%",
        "New Content Percentage": f"{new_content_percentage:.2f}%",
        "Topic Shift Impact": f"{topic_shift_impact:.2f}%"
    }

    return stats 
