from sentence_transformers import SentenceTransformer

# Loads 2 models

# According to sbert documentation
# The all-* models were trained on all available training data (more than 1 billion training pairs) and are designed as general purpose models. The all-mpnet-base-v2 model provides the best quality, while all-MiniLM-L6-v2 is 5 times faster and still offers good quality.
def load_models():
    model1 = SentenceTransformer("all-MiniLM-L6-v2")
    model2 = SentenceTransformer("all-mpnet-base-v2")
    return model1, model2

