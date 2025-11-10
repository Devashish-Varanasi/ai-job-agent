# test_gpt4all.py
# Simple script to test GPT4ALL installation and model loading

import os
from config import LOCAL_LLM_MODEL_PATH

def test_gpt4all_installation():
    print("Testing GPT4ALL installation...")
    
    # Check if gpt4all package is installed
    try:
        from gpt4all import GPT4All
        print("✓ GPT4ALL package is installed")
    except ImportError:
        print("✗ GPT4ALL package is not installed")
        print("  Run: pip install gpt4all")
        return
    
    # Check if model file exists
    if os.path.exists(LOCAL_LLM_MODEL_PATH):
        print(f"✓ Model file found at: {LOCAL_LLM_MODEL_PATH}")
    else:
        print(f"✗ Model file not found at: {LOCAL_LLM_MODEL_PATH}")
        print("  Please download a GPT4ALL model and place it in the models/ directory")
        print("  Then update LOCAL_LLM_MODEL_PATH in config.py")
        return
    
    # Try to load the model
    try:
        print("Loading model (this may take a moment)...")
        model = GPT4All(LOCAL_LLM_MODEL_PATH)
        print("✓ Model loaded successfully")
        
        # Test generation
        print("Testing generation...")
        response = model.generate("Hello, how are you?", max_tokens=20)
        print(f"✓ Generation successful: {response}")
        print("\nGPT4ALL is ready to use!")
        
    except Exception as e:
        print(f"✗ Error loading or using model: {e}")
        print("  Check that your model file is not corrupted")

if __name__ == "__main__":
    test_gpt4all_installation()