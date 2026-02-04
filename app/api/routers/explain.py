from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.retriever import retrieve_context
from app.llm.client import generate
from app.llm.prompts import anomaly_explanation_prompt

router = APIRouter(prefix="/explain-anomaly", tags=["GenAI"])

class ExplainRequest(BaseModel):
    anomaly_output: dict

@router.post("")
def explain(req: ExplainRequest):
    context, sources = retrieve_context(
        "cpu spike anomaly root cause and mitigation"
    )

    prompt = anomaly_explanation_prompt(req.anomaly_output, context)
    explanation = generate(prompt)

    return {
        "explanation": explanation,
        "sources": sources
    }

