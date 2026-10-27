import os
import subprocess
import requests

# Your live public ngrok API URL
API_URL = "https://stonework-unleaded-justly.ngrok-free.dev/generate"

print("==================================================")
print("⚡ LEOBRAIN FULLY AUTO-DEBUGGING AGENT")
print("==================================================")

task = input("\nWhat do you want Leobrain to build and run? (e.g., 'Write a python script that calculates factorial and has an intentional bug to test debugging'): ")
filename = input("Filename to save and execute? (e.g., 'test_bug.py'): ")

MAX_ATTEMPTS = 3
attempt = 1
current_prompt = f"### Instruction:\nWrite a clean, executable Python script for the following task: {task}. Return ONLY valid Python code without markdown code blocks if possible, or just the raw code.\n\n### Response:\n"

while attempt <= MAX_ATTEMPTS:
    print(f"\n🤖 [Attempt {attempt}/{MAX_ATTEMPTS}] Leobrain is generating/fixing your code...")
    
    payload = {
        "prompt": current_prompt,
        "max_new_tokens": 600
    }
    
    response = requests.post(API_URL, json=payload)
    
    if response.status_code != 200:
        print(f"❌ API Error {response.status_code}: {response.text}")
        break
        
    code_text = response.json().get("response", "")
    
    # Clean up markdown code blocks if the model included them
    if "```python" in code_text:
        code_text = code_text.split("```python")[1].split("```")[0]
    elif "```" in code_text:
        code_text = code_text.split("```")[1].split("```")[0]

    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code_text.strip())
    print(f"✅ Code saved to {filename}. Executing...")

    # Run the code locally
    result = subprocess.run(["python", filename], capture_output=True, text=True)

    if result.returncode == 0:
        print("\n--- EXECUTION OUTPUT ---")
        print(result.stdout)
        print(f"🎉 Success! The script executed perfectly on attempt {attempt}.")
        break
    else:
        print("\n❌ Execution Failed with Error:")
        print(result.stderr)
        
        if attempt < MAX_ATTEMPTS:
            print("🔄 Feeding error back to Leobrain for auto-debugging...")
            # Feed the error traceback back to Leobrain to fix!
            current_prompt = f"### Instruction:\nThe following Python script you wrote crashed with an error. Please fix the code and return ONLY the corrected Python script.\n\nTask: {task}\n\nError Traceback:\n{result.stderr}\n\n### Response:\n"
            attempt += 1
        else:
            print("❌ Max auto-debugging attempts reached. Manual intervention needed.")
            break