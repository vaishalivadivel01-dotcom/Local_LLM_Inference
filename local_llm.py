
import pandas as pd
import requests

# Read prompts
df = pd.read_csv("dataset/prompts.csv")

responses = []

url = "http://localhost:11434/api/generate"

for index, row in df.iterrows():

    prompt = row["prompt"]

    print(f"\nProcessing Prompt {row['id']}...")

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    result = response.json()

    answer = result["response"]

    responses.append({
        "id": row["id"],
        "prompt": prompt,
        "response": answer
    })

    print("Response generated successfully!")

# Save responses
output = pd.DataFrame(responses)

output.to_csv(
    "dataset/llm_responses.csv",
    index=False
)

# Save conversation history
with open("dataset/conversation_history.txt", "w", encoding="utf-8") as file:

    for item in responses:
        file.write(f"Prompt: {item['prompt']}\n")
        file.write(f"Response: {item['response']}\n")
        file.write("-" * 50 + "\n")

print("\nAll responses generated successfully!")
print("Responses saved in llm_responses.csv")
print("Conversation saved in conversation_history.txt")
