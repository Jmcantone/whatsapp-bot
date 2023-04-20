import os
import requests
from flask import Flask, request
import messagebird
from config import MESSAGEBIRD_API_KEY, LATITUDE, LONGITUDE, WHATSAPP_PHONE_NUMBER


app = Flask(__name__)

# Función para obtener información del clima
def get_weather_data():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'An error occurred while fetching weather data: {response.status_code}')
        return None

# Función para enviar un mensaje de WhatsApp
def send_whatsapp_message(phone_number, message):
    client = messagebird.Client(MESSAGEBIRD_API_KEY)
    try:
        message = client.messages.create(
            from_='InfoBot',
            to=phone_number,
            body=message,
            params={'type': 'text'}
        )
        return message
    except messagebird.client.ErrorException as e:
        print(f'An error occurred while sending the message: {e}')
        return None

@app.route('/send_weather', methods=['POST'])
def send_weather():
    weather_data = get_weather_data()

    if not weather_data:
        message = 'Unable to fetch weather data.'
    else:
        temp = weather_data['hourly']['temperature_2m'][0]  # Obtiene la temperatura actual
        message = f'The current temperature at lat {LATITUDE}, lon {LONGITUDE} is {temp}°C.'

    send_whatsapp_message(WHATSAPP_PHONE_NUMBER, message)

    return "Message sent", 200

if __name__ == "__main__":
    app.run(debug=True)
