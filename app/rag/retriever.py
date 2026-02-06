import os
from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOC_PATH = "app/data/docs"

def load_docs():
    texts, sources = [], []
    if not os.path.isdir(DOC_PATH):
        return texts, sources

    for fname in os.listdir(DOC_PATH):
        fpath = os.path.join(DOC_PATH, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            texts.append(f.read())
            sources.append(fname)

    return texts, sources

_vectorizer = None
_matrix = None
_texts = None
_sources = None

def get_index():
    global _vectorizer, _matrix, _texts, _sources

    if _matrix is None:
        _texts, _sources = load_docs()
        _vectorizer = TfidfVectorizer(stop_words="english")
        _matrix = _vectorizer.fit_transform(_texts)

    return _vectorizer, _matrix, _texts, _sources

@lru_cache(maxsize=64)
def retrieve_context(query: str, k: int = 2):
    vectorizer, matrix, texts, sources = get_index()
    if not texts:
        return "", []

    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, matrix).flatten()

    top_idx = sims.argsort()[-k:][::-1]
    context = "\n\n".join([texts[i] for i in top_idx])
    srcs = [sources[i] for i in top_idx]

    return context, srcs

