from dotenv import load_dotenv
import os

load_dotenv()

print("API URL:", os.getenv("API_FOOTBALL_URL"))
print("API key:", os.getenv("API_FOOTBALL_KEY"))
print("DB URL:", os.getenv("DB_URL"))
print("TZ:", os.getenv("TZ"))
