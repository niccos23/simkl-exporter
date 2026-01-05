import json
import os
import requests
import pandas as pd
from datetime import datetime
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
    
    today = datetime.now().strftime("%Y-%m-%d")

    stats = {
        "movies": 0,
        "tv": 0,
        "anime": 0
    }

    print(f"Starting Simkl data export for [{today}] using Client ID: {CLIENT_ID[:5]}...")

    # Iterate through our map
    for url_slug, json_key in media_map.items():
        print(f"Fetching {url_slug}...")
        response = requests.get(f"{base_url}/{url_slug}", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            full_export[url_slug] = data
            
            items_list = data.get(json_key, [])
            item_count = len(items_list)
            print(f"  > Found {item_count} items.")

            if url_slug in stats:
                stats[url_slug] = item_count
            
            if items_list and len(items_list) > 0:
                 # 1. Convert the raw list of dictionaries into a Pandas DataFrame (a table)
                df = pd.DataFrame(items_list)
                
                # 2. Create a filename, e.g., "simkl_movies_2025-01-04.csv"
                csv_filename = f"simkl_{url_slug}_{today}.csv"
                
                # 3. Save the dataframe to a CSV file without the index numbers (0,1,2...) on the left
                df.to_csv(csv_filename, index=False, encoding='utf-8')
                print(f"  > Saved CSV: {csv_filename}")
            # ----------------------------
        else:
            print(f"  > Error {response.status_code}: {response.text}")

    # --- Final JSON Save (Cleanup) ---
    # We already calculated 'today' at the start, so just use it here.
    json_filename = f"simkl_master_export_{today}.json"

    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(full_export, f, indent=4)
    
    print(f"\nSuccess! Master JSON backup saved to {json_filename}")
    print("Individual CSV files have also been created in this folder.")

    # --- NEW: Final Statistics Dashboard ---
    total_items = stats['movies'] + stats['tv'] + stats['anime']

    print(f"\n{'='*30}")
    print(f"📊  YOUR SIMKL STATS DASHBOARD")
    print(f"{'='*30}")
    print(f"🎬  Movies:      {stats['movies']}")
    print(f"📺  TV Shows:    {stats['tv']}")
    print(f"🍥  Anime:       {stats['anime']}")
    print(f"{'-'*30}")
    print(f"🏆  GRAND TOTAL: {total_items} Items")
    print(f"{'='*30}\n")
    # ---------------------------------------

if __name__ == "__main__":
    export_simkl_data()
    