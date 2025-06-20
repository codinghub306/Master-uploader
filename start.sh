#!/bin/bash

# Export env vars if .env exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Start Flask API + Telegram bot
gunicorn app:app &  # Flask server
python3 main.py     # Pyrogram bot
