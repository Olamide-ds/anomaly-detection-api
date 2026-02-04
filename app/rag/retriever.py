import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DOC_PATH = "app/data/docs"
MODEL_NAME = "all-MiniLM-L6-v2"

_model = None
_index = None
_texts = None
_sources = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def load_docs():
    texts, sources = [], []

    for fname in os.listdir(DOC_PATH):
        fpath = os.path.join(DOC_PATH, fname)
        if not os.path.isfile(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            texts.append(f.read())
            sources.append(fname)

    return texts, sources

def get_index():
    global _index, _texts, _sources

    if _index is None:
        model = get_model()
        _texts, _sources = load_docs()
        embeddings = model.encode(_texts)

        _index = faiss.IndexFlatL2(embeddings.shape[1])
        _index.add(np.array(embeddings))

    return _index, _texts, _sources

def retrieve_context(query: str, k: int = 2):
    model = get_model()
    index, texts, sources = get_index()

    q_emb = model.encode([query])
    _, I = index.search(np.array(q_emb), k)

    context = "\n\n".join([texts[i] for i in I[0]])
    srcs = [sources[i] for i in I[0]]

    return context, srcs

