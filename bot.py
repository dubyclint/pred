# bot.py

import telebot
import os
import html
import requests # New import for making HTTP requests
import json     # New import for handling JSON data

# Your Telegram Bot Token - MUST be set as an environment variable
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Telegram bot token not found in environment — set TELEGRAM_BOT_TOKEN")

# The URL of your deployed Gemini ADK Agent (e.g., on Railway)
# You MUST replace this with the actual URL from your Railway deployment.
# Example: "https://your-service-name-xxxx.up.railway.app"
ADK_AGENT_URL = os.getenv("ADK_AGENT_URL")
if not ADK_AGENT_URL:
    raise ValueError("ADK Agent URL not found in environment — set ADK_AGENT_URL")

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Handles the /start and /help commands, sending a welcome message.
    """
    welcome_text = (
        "<b>🔮 Sports Match Predictor Bot</b>\n\n"
        "📥 I'm powered by a Gemini ADK Agent! Just specify sport + teams:\n"
        "- <code>basketball: Crvena Zvezda vs Partizan</code>\n"
        "- <code>football: PSG vs Botafogo</code>\n"
        "- <code>tennis: Rafael Nadal vs Novak Djokovic</code>\n"
        "- <code>cricket: India vs England</code>\n"
        "The ADK Agent will process your request and provide a prediction."
    )
    bot.reply_to(message, welcome_text, parse_mode='html')

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    """
    Handles all incoming text messages, sending them to the ADK Agent for prediction.
    """
    user_query = message.text.strip()
    chat_id = message.chat.id

    bot.send_chat_action(chat_id, 'typing') # Show "typing..." status

    try:
        # Construct the payload for the ADK agent.
        # The ADK web UI expects a 'text' field for the user query.
        payload = {"text": user_query}
        headers = {"Content-Type": "application/json"}

        # Make a POST request to your deployed ADK Agent
        response = requests.post(f"{ADK_AGENT_URL}/chat", headers=headers, data=json.dumps(payload))
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        agent_response = response.json()

        # The ADK agent's response structure might vary.
        # Assuming the ADK agent returns a 'text' field with the prediction.
        # If your ADK agent returns a structured JSON, you'll need to parse it here.
        if 'text' in agent_response:
            output = agent_response['text']
            bot.reply_to(message, html.escape(output), parse_mode='html')
        else:
            bot.reply_to(message, "🚨 The ADK Agent returned an unexpected response format.", parse_mode='html')
            print("ADK Agent raw response:", agent_response)

    except requests.exceptions.RequestException as req_err:
        bot.reply_to(message, f"🚨 Error connecting to the prediction service: {html.escape(str(req_err))}", parse_mode='html')
        print("Request error:", req_err)
    except json.JSONDecodeError as json_err:
        bot.reply_to(message, f"🚨 Error parsing response from prediction service: {html.escape(str(json_err))}", parse_mode='html')
        print("JSON decode error:", json_err)
    except Exception as e:
        bot.reply_to(message, "🚨 An unexpected error occurred while processing your request.", parse_mode='html')
        print("General error:", str(e))

if __name__ == "__main__":
    print("🚀 Starting Telegram bot...")
    try:
        # Start polling for new messages. none_stop=True keeps it running.
        bot.polling(none_stop=True)
    except Exception as e:
        print("❌ Bot failed to start:", str(e))
