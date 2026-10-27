# Leobrain 🧠🚀

Leobrain is an autonomous coding assistant powered by a fine-tuned open-source LLM (`Qwen2.5-Coder-7B-Instruct`), trained using Unsloth and QLoRA adapters on Google Colab, and hosted via a FastAPI server with ngrok tunneling.

## Project Structure
- `training/`: Contains the Google Colab training notebook (`train_colab.ipynb`).
- `inference/`: Contains the FastAPI server script (`api_server.py`) for online deployment.

## How It Works
1. **Fine-Tuning:** Trained on custom coding datasets using LoRA adapters for memory efficiency on a T4 GPU.
2. **API Hosting:** Deployed locally in Colab and exposed globally via an ngrok public endpoint for real-time agent requests.