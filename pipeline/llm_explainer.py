import subprocess

def explain_with_gemma(text: str) -> str:
    prompt = f"""
You are a public health assistant.
Explain the health implications of the following situation:

{text}
"""
    result = subprocess.run(
        ["ollama", "run", "gemma3:4b"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()
