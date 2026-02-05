def anomaly_explanation_prompt(anomaly_output, context):
    return f"""
You are an SRE AI assistant.

Analyze the anomaly output and context below.

Anomaly output:
{anomaly_output}

Context:
{context}

Return ONLY valid JSON.
DO NOT include markdown.
DO NOT include explanations.
DO NOT wrap the JSON in quotes.
DO NOT include ```.

JSON schema:
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
"""

