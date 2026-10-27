import requests

# Your live public ngrok API URL from Google Colab
API_URL = "https://stonework-unleaded-justly.ngrok-free.dev/generate"

print("==================================================")
print("💬 CONNECTED TO LEOBRAIN CHAT INTERFACE")
print("Type your coding prompt below or type 'exit' to quit.")
print("==================================================")

while True:
    # Get prompt from user input in the terminal
    user_prompt = input("\nPrompt > ")
    
    # Exit condition
    if user_prompt.lower() in ["exit", "quit"]:
        print("Closing Leobrain chat. Goodbye!")
        break
        
    if not user_prompt.strip():
        continue

    # Format prompt for your instruction-tuned model
    formatted_prompt = f"### Instruction:\n{user_prompt}\n\n### Response:\n"
    
    payload = {
        "prompt": formatted_prompt,
        "max_new_tokens": 400
    }

    print("🤖 Leobrain is thinking...")
    
    try:
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print("\n----------------------------------")
            print(data.get("response", "No response returned."))
            print("----------------------------------")
        else:
            print(f"\n❌ Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"\n❌ Connection failed: {e}")