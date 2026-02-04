def anomaly_explanation_prompt(anomaly_output: dict, context: str) -> str:
    return f"""
You are a senior site reliability and data analyst.

An anomaly was detected with the following details:
{anomaly_output}

Relevant operational documentation:
{context}

Tasks:
1. Identify the most likely root cause(s).
2. Describe potential operational or business impact.
3. Recommend concrete next actions.
4. Clearly state assumptions and uncertainty.

Be concise, structured, and grounded ONLY in the provided context.
"""

