# **Simkl Data Exporter 🎬**

A robust, open-source Python tool to export your entire watch history (Movies, TV Shows, and Anime) from [Simkl](https://simkl.com/) to local JSON backup files.  
Unlike other tools, this script handles large libraries and Simkl's specific API quirks (like "TV" vs "Shows" mapping) automatically.

## **✨ Features**

* **🔒 Secure:** Runs locally using OAuth 2.0. Your password never leaves your machine.  
* **📅 Daily Snapshots:** Automatically timestamps backups (e.g., simkl\_export\_2025-01-02.json) so you never overwrite your history.  
* **✅ Complete:** Exports all three categories: Movies, TV Shows, and Anime.  
* **🚀 Automation Ready:** Designed to be run manually or scheduled via cron/GitHub Actions.

## **🛠️ Installation**

1. **Clone the repository**  
   git clone \[https://github.com/niccos23/simkl-exporter.git\](https://github.com/niccos23/simkl-exporter.git)  
   cd simkl-exporter

2. **Install Dependencies**  
   pip install \-r requirements.txt

3. Setup Credentials  
   Create a .env file in the project folder with your Simkl keys.  
   (See env.example if available or use the format below):  
   SIMKL\_CLIENT\_ID=your\_client\_id\_here  
   SIMKL\_ACCESS\_TOKEN=your\_access\_token\_here  
   💡 Need a token?  
   If you don't have an Access Token yet, run the included helper script and follow the instructions:python auth.py

## **🚀 Usage**

Run the export script from your terminal:  
python main.py

### **Output**

The script will generate a JSON file with today's date in the filename:  
📂 simkl\_export\_YYYY-MM-DD.json

## **🔮 Roadmap**

* \[x\] JSON Export with Timestamps  
* \[ \] CSV / Excel Export (Coming Soon)  
* \[ \] Watch Statistics Dashboard

## **📄 License**

MIT © [niccos23](https://www.google.com/search?q=https://github.com/niccos23)