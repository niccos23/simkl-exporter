import os
import requests
import json
from dotenv import load_dotenv

# Load keys from .env
load_dotenv()

CLIENT_ID = os.getenv("SIMKL_CLIENT_ID")
CLIENT_SECRET = os.getenv("SIMKL_CLIENT_SECRET")
REDIRECT_URI = "https://simkl.com"

def get_new_token():
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Error: Please make sure SIMKL_CLIENT_ID and SIMKL_CLIENT_SECRET are in your .env file.")
        return

    # 1. Generate the authorization URL
    auth_url = (
        f"https://simkl.com/oauth/authorize?"
        f"response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    )
    
    print("\n--- ACTION REQUIRED ---")
    print("1. Click (or copy) this URL to authorize your app:")
    print(auth_url)
    print("\n2. Click 'Authorize'. You will see a code on the screen.")
    
    # 2. User pastes the code
    code = input("3. Paste the code here and press Enter: ").strip()
    
    # 3. Exchange code for Access Token
    token_url = "https://api.simkl.com/oauth/token"
    payload = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    
    print("\nRequesting token...")
    response = requests.post(token_url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        new_token = data.get("access_token")
        print("\nSUCCESS! Here is your new Access Token:")
        print("-" * 60)
        print(new_token)
        print("-" * 60)
        print(">> Copy this token and paste it into your .env file as SIMKL_ACCESS_TOKEN")
    else:
        print(f"\nError: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_new_token()
