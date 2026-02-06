def anomaly_explanation_prompt(anomaly_output: dict, context: str) -> str:
    return f"""
Return ONLY valid JSON (no markdown, no backticks, no commentary).
Do NOT wrap the JSON in quotes.

Schema (must match exactly):
{{
  "root_causes": [string],
  "impact": {{
    "operational": string,
    "business": string
  }},
  "recommended_actions": [string],
  "assumptions": [string],
  "uncertainty": string
}}

anomaly_output:
{anomaly_output}

context:
{context}
"""

