def extract_topics(syllabus):
    if "course_content" not in syllabus:
        raise ValueError("Course Content is missing in the data.")
    
    syllabus_data = syllabus["course_content"]
    topics = []

    for unit_name, unit in syllabus_data.items():
        if isinstance(unit, dict) and 'title' in unit and 'topics' in unit:
            for topic in unit['topics']:
                topics.append((topic, unit_name, unit['title']))
    
    return topics
