# Simkl Data Exporter

A simple, robust Python script to export your entire watch history (Movies, TV Shows, and Anime) from [Simkl](https://simkl.com/) to a local JSON file.

## Features
- ✅ **Secure:** Uses OAuth 2.0 (no password sharing).
- ✅ **Accurate:** Correctly handles Simkl API quirks (like "TV" vs "Shows").
- ✅ **Complete:** Exports Movies, TV Shows, and Anime.

## Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/niccos23/simkl-exporter.git](https://github.com/niccos23/simkl-exporter.git)
   cd simkl-exporter
2. **Install Dependencies**
    pip install -r requirements.txt
3. **Setup Credentials Create a .env file in the project folder with your Simkl keys:**
    SIMKL_CLIENT_ID=your_client_id_here
    SIMKL_ACCESS_TOKEN=your_access_token_here
Need a token? Run the included auth script:

    Bash

python auth.py

Usage

Run the export script:
Bash

python main.py

License

MIT


