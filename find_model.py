# find_model.py
# Script to help locate the GPT4ALL model file

import os
from pathlib import Path

def find_gpt4all_models():
    print("Searching for GPT4ALL model files...\n")
    
    # Common locations where GPT4ALL stores models
    possible_locations = [
        os.path.join(os.environ.get('LOCALAPPDATA', ''), 'nomic.ai', 'GPT4All'),
        os.path.join(os.environ.get('APPDATA', ''), 'nomic.ai', 'GPT4All'),
        os.path.join(os.path.expanduser('~'), '.cache', 'gpt4all'),
        os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'nomic.ai', 'GPT4All'),
    ]
    
    found_models = []
    
    for location in possible_locations:
        if os.path.exists(location):
            print(f"Checking: {location}")
            for root, dirs, files in os.walk(location):
                for file in files:
                    if file.endswith(('.gguf', '.bin')):
                        model_path = os.path.join(root, file)
                        found_models.append(model_path)
                        print(f"  Found: {file}")
                        print(f"  Full path: {model_path}\n")
    
    if not found_models:
        print("No model files found in common locations.")
        print("\nPlease check where GPT4ALL downloaded the model:")
        print("1. Open GPT4ALL application")
        print("2. Go to Settings/Models")
        print("3. Check the model download location")
        print("4. Copy the model file to your project's 'models' directory")
    else:
        print(f"\n{len(found_models)} model file(s) found!")
        print("\nTo use a model:")
        print("1. Copy the model file to your project's 'models' directory, OR")
        print("2. Update LOCAL_LLM_MODEL_PATH in config.py with the full path above")
    
    return found_models

if __name__ == "__main__":
    find_gpt4all_models()
