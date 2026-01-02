import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("SIMKL_ACCESS_TOKEN")
client_id = os.getenv("SIMKL_CLIENT_ID")

print("\n--- DEBUGGING SECRETS ---")

if token:
    print(f"Token Length: {len(token)}")
    print(f"First 4 chars: '{token[:4]}'")
    print(f"Last 4 chars:  '{token[-4:]}'")
    
    # CHECK FOR COMMON MISTAKES
    if token.startswith('"') or token.startswith("'"):
        print("❌ ERROR: Your token in .env starts with a quote. Remove it!")
    elif token.endswith(" "):
        print("❌ ERROR: Your token in .env has a hidden space at the end. Delete it!")
    else:
        print("✅ Format looks clean (no quotes or spaces).")
else:
    print("❌ ERROR: Python cannot find SIMKL_ACCESS_TOKEN in .env at all.")

print("-" * 30)