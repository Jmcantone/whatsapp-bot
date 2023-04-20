# WhatsApp Bot for Daily Reminders

This project is a simple WhatsApp bot that sends daily reminders including Google Calendar events, Trello tasks, and weather information. The bot is built using Python, Flask, and integrates with various APIs such as MessageBird, Google Calendar, and Trello.

## Prerequisites

Before you begin, make sure you have the following:

- Python 3.6 or higher
- A MessageBird account and API key
- Google API credentials for Google Calendar
- Trello API credentials (optional, if you want to include Trello tasks)
- Weather API credentials (optional, if you want to include weather information)

## Installation

1. Clone this repository.

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Create a `config.py` file in the project directory and add your API credentials:

```python
MESSAGEBIRD_API_KEY = "your_messagebird_api_key"
GOOGLE_CALENDAR_CREDENTIALS = "path/to/credentials.json"
WHATSAPP_PHONE_NUMBER = "whatsapp:your_phone_number"
```

5. Add config.py to .gitignore to exclude it from the repository.

## Usage
1. Run the Flask server:
python app.py
2. Send a POST request to the /send_reminder endpoint to trigger the bot:
curl -X POST http://127.0.0.1:5000/send_reminder
3. Configure a cron job or scheduled task to run the bot daily at a specific time.

## Customization
This project is a basic example and can be extended to include more features or integrate with other APIs. Feel free to customize it according to your needs.
