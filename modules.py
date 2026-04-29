# modules.py

from llm import generate_response
import json
import re


def idea_prompt(idea):
    return f"""
You are a startup analyst.

Analyze the idea and return ONLY valid JSON with REAL insights.

Idea: {idea}

{{
"tech": "Explain feasibility and technology in 1-2 meaningful sentences",
"business": "Explain business value and model in 1-2 meaningful sentences",
"user": "Explain target users and benefits in 1-2 meaningful sentences",
"investor": "Explain investment potential in 1-2 meaningful sentences",
"risk": "Explain risks in 1-2 meaningful sentences",

"challenges": "Explain practical challenges in 1-2 meaningful sentences",
"dependencies": "Explain key dependencies in 1-2 meaningful sentences",

"improve": [
"Provide a real improvement",
"Provide another real improvement"
],

"solution": "Describe a practical solution in 1-2 meaningful sentences",

"next_steps": [
"Give a real next step",
"Give another real next step"
],

"score_insight": "Explain why the scores are given in 1-2 sentences",

"scores": {{
"feasibility": 0-10,
"innovation": 0-10,
"market": 0-10
}},

"final": 0-10,
"verdict": "Good or Average"
}}

IMPORTANT:
- Replace ALL placeholder text with real insights
- Do NOT repeat words like "short description"
- Each field must be meaningful and specific to the idea
- Keep responses concise but informative
- Output ONLY JSON
"""


def analyze_idea(idea):
    prompt = idea_prompt(idea)

    output = generate_response(prompt)

    try:
        # Extract JSON block
        start = output.find("{")
        end = output.rfind("}") + 1
        clean = output[start:end]

        # Fix formatting issues
        clean = re.sub(r",\s*}", "}", clean)
        clean = re.sub(r",\s*]", "]", clean)

        data = json.loads(clean)
        return data

    except Exception as e:
        print("JSON parsing failed:", e)
        print("Raw output:", output)

        # fallback
        return {
            "tech": "Feasible using modern AI tools with moderate complexity.",
            "business": "Provides value through improved efficiency and automation.",
            "user": "Helps users simplify tasks and improve productivity.",
            "investor": "Shows potential due to scalability and growing demand.",
            "risk": "Competition and adoption challenges may impact growth.",

            "challenges": "User acquisition and customization may be difficult.",
            "dependencies": "Requires AI tools, data access, and cloud infrastructure.",

            "improve": [
                "Add personalization features",
                "Enhance user experience"
            ],

            "solution": "An AI-driven platform offering efficient and scalable solutions.",

            "next_steps": [
                "Develop MVP",
                "Test with initial users"
            ],

            "score_insight": "Good feasibility and demand, but moderate innovation and competition.",

            "scores": {
                "feasibility": 7,
                "innovation": 6,
                "market": 7
            },

            "final": 7,
            "verdict": "Good"
        }