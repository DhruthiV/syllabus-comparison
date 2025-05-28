# Syllabus Comparison

A Python package to compare old and new syllabi using NLP-based semantic similarity.

## Features
- Detects **added** and **removed** topics.
- Identifies **semantic matches** and **elaborations**.
- Finds **shifted topics** (topics moved between units).
- Uses Pretrained [Sentence Transformers](https://www.sbert.net/) (all-MiniLM-L6-v2 and also all-mpnet-base-v2) for comparison. 

## Installation

```sh
pip install git+https://github.com/DhruthiV/syllabus-comparison.git
```

## Upgrading to the Latest Version
To upgrade to the latest version from GitHub, run:
```sh
pip install --upgrade git+https://github.com/DhruthiV/syllabus-comparison.git
```
## Future Enhancements

Domain-Specific Model Training: As a near-future enhancement, we can fine-tune the NLP model with domain-specific terms from PESU syllabi. 
This will improve semantic similarity scores and provide more accurate matching results.
