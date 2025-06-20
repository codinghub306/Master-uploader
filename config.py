import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Ensure correct key name
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN is missing from environment variables.")
        
    API_ID = int(os.environ.get("API_ID", "20928172"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "48ed56c8db54f85d232f576b150360ef")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6443740402").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "Shreya")  # Making CREDIT an environment variable for flexibility
