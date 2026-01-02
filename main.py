import os
import json
import requests
from dotenv import load_dotenv

# 1. Load the keys
load_dotenv()

CLIENT_ID = os.getenv("SIMKL_CLIENT_ID")
ACCESS_TOKEN = os.getenv("SIMKL_ACCESS_TOKEN")

def export_simkl_data():
    if not CLIENT_ID or not ACCESS_TOKEN:
        print("Error: Keys are missing. Check your .env file.")
        return

    base_url = "https://api.simkl.com/sync/all-items"
    
    # 2. Map the URL slug (key) to the JSON response key (value)
    # Simkl returns 'shows' when you ask for 'tv'
    media_map = {
        "movies": "movies",
        "tv": "shows",
        "anime": "anime"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "simkl-api-key": CLIENT_ID
    }

    full_export = {}

    print(f"Starting Simkl data export using Client ID: {CLIENT_ID[:5]}...")

    # Iterate through our map
    for url_slug, json_key in media_map.items():
        print(f"Fetching {url_slug}...")
        response = requests.get(f"{base_url}/{url_slug}", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            full_export[url_slug] = data
            
            # Count the items using the CORRECT key
            item_count = len(data.get(json_key, []))
            print(f"  > Found {item_count} items.")
        else:
            print(f"  > Error {response.status_code}: {response.text}")

    # Save to a local file
    filename = "simkl_export.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(full_export, f, indent=4)
    
    print(f"\nSuccess! Data exported to {filename}")

if __name__ == "__main__":
    export_simkl_data()
    