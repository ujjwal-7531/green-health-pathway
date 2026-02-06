from pipeline.llm_explainer import explain_with_gemma

print("\nPublic Health Alert Chat (type 'exit' to quit)\n")

# Optional: initial alert context
base_context = (
    "Area Zone_C has HIGH public health risk. "
    "AQI is 182, temperature is 36.5°C, wind speed is 0.8 m/s."
)

while True:
    user_input = input("You: ")

    if user_input.lower() in ("exit", "quit"):
        print("Exiting chat.")
        break

    # Combine alert + follow-up question
    full_prompt = base_context + "\n\nUser question: " + user_input

    response = explain_with_gemma(full_prompt)
    print("\nGemma:\n", response, "\n")
