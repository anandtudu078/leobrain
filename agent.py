import os
import requests

# Your live public ngrok API URL
API_URL = "https://stonework-unleaded-justly.ngrok-free.dev/generate"

print("==================================================")
print("🤖 LEOBRAIN AUTONOMOUS CODE AGENT")
print("==================================================")

# Get input from user
task_description = input("\nWhat do you want Leobrain to build? (e.g., 'Write a python script for a simple calculator'): ")
filename = input("What should be the filename? (e.g., 'calculator.py'): ")

# Format the prompt
formatted_prompt = f"### Instruction:\n{task_description}\n\n### Response:\n"

payload = {
    "prompt": formatted_prompt,
    "max_new_tokens": 500
}

print("\n🚀 Leobrain is generating and writing your code...")

try:
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        generated_code = data.get("response", "")
        
        # Clean up the output if needed and save to file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(generated_code)
            
        print(f"\n✅ Success! Code successfully written and saved to: {filename}")
    else:
        print(f"\n❌ Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"\n❌ Connection failed: {e}")