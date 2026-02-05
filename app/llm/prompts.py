def anomaly_explanation_prompt(anomaly_output: dict, context: str) -> str:
    return f"""
You are an SRE-focused AI assistant.

Using the anomaly output and the provided operational context, produce a
STRICT JSON response with the following structure:

{{
  "root_causes": [string],
  "impact": [string],
  "recommended_actions": [string],
  "assumptions": [string]
}}

Rules:
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations outside the JSON
- Each list should contain 2–5 concise bullet-style strings

Anomaly Output:
{anomaly_output}

Operational Context:
{context}
"""

